import IPython
import random

'''
This it the stock object. You use this by giving the value of
stocks bought and sold with trade function. After that you tick
the date forward by one with tick function. get_price() function
return the price of the day.
'''

class Stock:
    def __init__(self, price=100):
        self.pool = 10000
        self.price = price
        self.prevprice = 0
        self.baseline = self.price
        self.sales = 0
        self.buys = 0
        self.day = 0

    def trade(self, buys=0, sales=0):
        # One day's net trading
        self.sales += sales
        self.buys += buys

    def get_price(self):
        # get today's price
        return self.price

    def get_pool(self):
        return self.pool

    def get_buys(self):
        return self.buys

    def get_sales(self):
        return self.sales

    def get_date(self):
        return self.day

    def tick(self):
        # New day
        self.prevprice = self.price
        self.price = self.price * self.pool/float(self.pool-(2*(self.buys-(9/7)*self.sales)))
        self.price = self.price - (0.05*(self.price-self.baseline))
        self.sales = 0
        self.buys = 0
        self.day += 1
        if self.price < 0.05 * self.baseline:
            self.price = 0.05*self.baseline
        if abs(self.price-self.prevprice)/self.price > 0.2:
            if self.prevprice > self.price:
                self.price = 0.8 * self.prevprice
            else:
                self.price = 1.2 * self.prevprice
        self.price *= 1+random.normalvariate(0,0.04)
        
def main():
    s = Stock()
    for i in range(0,15):
        s.trade(sales=500)
        s.tick()
        print(s.get_price())
    print("")
    for i in range(0,15):
        s.tick()
        print(s.get_price())

if __name__ == "__main__":
    main()