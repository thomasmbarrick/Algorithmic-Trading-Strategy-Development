import backtrader


#This class adapts the test strategy from the Backtrader quickstart guide.
# https://www.backtrader.com/docu/quickstart/quickstart/#adding-some-logic-to-the-strategy
class TestStrategyAdapted(backtrader.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.bar_executed = 0
        
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        if order.status == order.Completed:
            if order.isbuy():
                self.log("BUY EXECUTED, Price: {}".format(order.executed.price))
            elif order.issell():
                self.log("SELL EXECUTED, Price: {}".format(order.executed.price))
            
            self.bar_executed = len(self)  
        
        self.order = None  
        
    
    def next(self):
        self.log('Close, %.2f' % self.dataclose[0])
        
        #Prevents buying/selling stock if there is an order being made
        if self.order:
            return
        
        #Prevents buying more stock if you already have stocks purchased
        if not self.position:
            if self.dataclose[0] < self.dataclose[-1]:
                if self.dataclose[-1] < self.dataclose[-2]:
                    self.log('BUY CREATED, %.2f' % self.dataclose[0])
                    self.order = self.buy()

        #Sells stock five days after the order is completed 
        elif len(self) >= (self.bar_executed + 5):
            self.log("SELL CREATED, %.2f" % self.dataclose[0])
            self.order = self.sell()
            print("Sell order placed")