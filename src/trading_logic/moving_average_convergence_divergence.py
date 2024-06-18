import backtrader

class MACD(backtrader.Strategy):
    
    def Log(self, txt, dt=None):
        '''Logging Function'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
        
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.bar_executed = 0
        
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        self.order = None
        
    def next(self):
        self.log('Close, %.2f' % self.dataclose[0])