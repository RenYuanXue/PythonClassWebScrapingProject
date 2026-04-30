# required libraries
import pandas as pd
from KeyChron import name_reviews

reviews, names = name_reviews()

c = pd.DataFrame({'name':names,
                  'review':reviews,
                 })
print(c.head)