import random
from stock import Stock

'''
Investor is the object which represents investing party.
Investor is meant to get stock object as an attibute in init function.
Investor will target all of its actions to that stock object only.
'''

class Investor:

    def __init__(self, id, personality, funds, stock):
        
        self.id = id
        self.personality = personality
        self.funds = funds                  # Funds available
        self.investedFunds = self.funds     # Used to calculate profits
        self.shares = 0                     # Share that this particular person owns
        self.stock = stock                  # This is the stock
        #self.has_invested = False           # This flag is set to true once the investor has exitedfrom the market

        if personality in ['smart money','institutional','householding']:
            if self.personality == "smart money":
                self.threshold_buy = random.randint(95, 200)
                self.threshold_sell = random.randint(1000, 1200)
                self.loss_sell = random.randint(40,80)/100
                self.profit_sell = random.randint(400,1300)/100
            elif self.personality == "institutional":
                self.threshold_buy = random.randint(150,400)
                self.threshold_sell = random.randint(1200, 1300)
                self.loss_sell = random.randint(40,80)/100
                self.profit_sell = random.randint(400,1300)/100
            else:
                self.threshold_buy = random.randint(350, 600)
                self.threshold_sell = random.randint(1200, 1500)
                self.loss_sell = random.randint(40,80)/100
                self.profit_sell = random.randint(400,1300)/100
        else:
            raise ValueError('Investor object personality has to be smart money, institutional or householding')

    def decide(self):
        # This function is called when investor has to make an investment decision
        # I.e. every 'day'
        if self.funds == 0:
            return
        if self.check_price() > self.threshold_buy:
            if self.check_profits() > self.profit_sell or self.check_price() > self.threshold_sell:
                self.sell(self.shares)
                self.funds = 0
                #print("Day: {2}: {1} investor {0} sold all!".format(self.id, self.personality, self.stock.get_date()))
                #self.has_invested = True
            elif self.check_profits() < self.loss_sell:
                self.sell(self.shares)
                self.funds = 0
                #print("Day: {2}: {1} investor {0} sold all!".format(self.id, self.personality, self.stock.get_date()))
                #self.has_invested = True
            elif self.funds > self.investedFunds/12:
                self.buy(self.investedFunds/12)
                #print("Day: {2}: {1} investor {0} bought stock!".format(self.id, self.personality, self.stock.get_date()))
            elif self.funds > 0:
                self.buy(self.funds)
                #print("Day: {2}: {1} investor {0} bought stock!".format(self.id, self.personality, self.stock.get_date()))
        

    def buy(self, amount):
        # buy shares of the stock given in init
        # amount here means the sum of money for the purchase
        if self.funds >= amount:
            purchase = amount / self.check_price()
            self.shares += purchase
            self.stock.trade(buys=purchase)
            self.funds -= amount
        else:
            raise ValueError("Can't buy this many shares")

    def sell(self, amount):
        # sell shares
        # 'amount' here means shares, not their value
        if self.shares >= amount:
            sale = amount * self.check_price()
            self.funds += sale
            self.stock.trade(sales=amount)
            self.shares -= amount
        else:
            raise ValueError("Can't sell this many shares")

    def check_price(self):
        return self.stock.get_price()

    def check_profits(self):
        if self.shares == 0:
            return 1
        return ((self.shares * self.check_price()) + self.funds) / self.investedFunds

    def get_buy_threshold(self):
        return self.threshold_buy

    def get_sell_threshold(self):
        return self.threshold_sell

    def get_shares(self):
        return self.shares

    def get_funds(self):
        return self.funds

def main():
    # This main is for testing Investor object

    s = Stock()
    prices = []

    smi = 30    # number of smart money investors
    iis = 50     # number of institutional investors
    hho = 500     # number of house hold investors

    smif = 10000    # smart money investor's funds
    iisf = 10000    # smart money investor's funds
    hhof = 100    # smart money investor's funds

    # I put my Investors object in an array, it's easier to handle them
    my_investors = []

    for i in range (1,smi):
        investor = Investor(i, "smart money", smif, s)
        my_investors.append(investor)

    for i in range (smi,iis+smi):
        investor = Investor(i, "institutional", iisf, s)
        my_investors.append(investor)

    for i in range (iis+smi,iis+smi+hho):
        investor = Investor(i, "householding", hhof, s)
        my_investors.append(investor)

    for day in range(0,1000):
        for inv in my_investors:
            inv.decide()
            s.tick()
        prices.append([day,s.get_price()])

    for p in prices:
        print(p[0],p[1])


if __name__ == "__main__":
    main()


