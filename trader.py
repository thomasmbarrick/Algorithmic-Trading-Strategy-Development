import backtrader
import datetime 
import sys
sys.path.append('src/trading_logic')
from test_strategy import TestStrategy
from test_strategy_adapted import TestStrategyAdapted
from moving_average_crossover import MovingAverageCrossover


cerebro = backtrader.Cerebro()

cerebro.broker.set_cash(1000000)

data = backtrader.feeds.YahooFinanceCSVData(
    dataname= r"historical_data\SP500_data.csv",
    fromdate = datetime.datetime(2000,1,1),
    todate = datetime.datetime(2024,1,1),
    reverse=False)

cerebro.adddata(data)
cerebro.addstrategy(MovingAverageCrossover)
cerebro.addsizer(backtrader.sizers.FixedSize, stake=500)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()