# required libraries
import pandas as pd
from KeyChron import name_reviews
from Prices import return_prices

reviews, names = name_reviews()
prices = return_prices

c = pd.DataFrame({'name':names,
                  'review':reviews,
                  'prices':prices
                 })
print(c.head)
