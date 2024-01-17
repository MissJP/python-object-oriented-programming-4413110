# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: use inheritance and abstract classes

# Challenge: create a class structure to represent stocks and bonds
# Requirements:
# DONE -- Both stocks and bonds have a price
# DONE -- Stocks have a company name and ticker
# DONE -- Bonds have a description, duration, and yield
# DONE -- You should not be able to instantiate the base class
# DONE -- Subclasses are required to override get_description()
# DONE -- get_description returns formats for stocks and bonds
# DONE For stocks: "Ticker: Company -- $Price"
# DONE For bonds: "description: duration'yr' : $price : yieldamt%"
from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_description(self):
        pass
    
class Stock(Asset):
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    def get_description(self):
        return f'{self.ticker}: {self.company} -- ${self.price}'

class Bond(Asset):
    def __init__(self, price, description, duration, interestrate):
        self.price = price
        self.description = description
        self.duration = duration
        self.interestrate = interestrate

    def get_description(self):
        return f"{self.description}: {self.duration}'yr' : ${self.price} : {self.interestrate}%"

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
try:
   ast = Asset(100.0)
except:
   print("Can't instantiate Asset!")

msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

us30yr = Bond(95.31, "30 Year US Treasury", 30, 4.38)
us10yr = Bond(96.70, "10 Year US Treasury", 10, 4.28)
us5yr = Bond(98.65, "5 Year US Treasury", 5, 4.43)
us2yr = Bond(99.57, "2 Year US Treasury", 2, 4.98)

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())
print('\n')
print(us30yr.get_description())
print(us10yr.get_description())
print(us5yr.get_description())
print(us2yr.get_description())
