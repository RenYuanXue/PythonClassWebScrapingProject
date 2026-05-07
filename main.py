# required libraries
import pandas as pd
from Colors import return_colors
from KeyChron import name_reviews
from Prices import return_prices

reviews, names = name_reviews()
prices = return_prices()
colors = return_colors()

if __name__ == "__main__":

    reviews, names = name_reviews()
    prices = return_prices()
    colors = return_colors()

    c = pd.DataFrame({'name':names,
                    'review':reviews,
                    'prices':prices,
                    'colors':colors
                    })

    c.to_csv('keychron.csv', index=False)