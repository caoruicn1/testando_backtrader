import backtrader as bt

def main():
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000.0)
    print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())

    cerebro.run()

    print("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())

if __name__ == '__main__':
    main()