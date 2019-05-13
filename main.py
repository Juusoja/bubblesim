from stock import Stock
#from csvwrite import CsvProcess
from investor import Investor
import matplotlib.pyplot as plt
import numpy as np

def main():
    s = Stock()
    prices = []

    smi = 300    # number of smart money investors
    iis = 500    # number of institutional investors
    hho = 8000   # number of house hold investors

    smif = 40000    # smart money investor's funds
    iisf = 80000    # institutional investor investor's funds
    hhof = 2000     # house hold investor's funds

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

    for day in range(0,150):
        for inv in my_investors:
            inv.decide()
        s.tick()
        prices.append([day,s.get_price()])

    for p in prices:
        print(p[0],p[1])

    #csvP = CsvProcess()
    #csvP.csvWrite(prices,'price.csv')
    
    numPrices = np.asarray(prices)
    plt.figure(1)
    plt.plot(numPrices[:,1])
    plt.xlabel('Time')
    plt.ylabel('Price')
    
    #plt.figure(2)
    #plt.plot(numPrices[0:60,1])
    #plt.xlabel('Time')
    #plt.ylabel('Price')
    plt.show()

if __name__ == "__main__":
    main()