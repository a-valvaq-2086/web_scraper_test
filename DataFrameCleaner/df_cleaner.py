import numpy as np
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, "en_US")


class MyDataFrameCleaner:
    """Class of that contains the cleaning methods for the headlines comming from the HTML parsing"""
    def __init__(self, df):
        self.df = df


    def date_cleaner(self, df):
        "Return the headlines dates as a Python date object in ISO format"
        
        d_months = {"Jan.": "January", "Feb.": "February", "Aug.": "August", "Sept.": "September",
         "Oct.": "October", "Nov.": "November", "Dec.": "December"}

        for key, val in d_months.items():
            df['Date'] = df['Date'].str.replace(key, val, regex=True)

        df['Date'] = pd.to_datetime(df['Date'], format="%B %d, %Y")

        return df


    def headline_cleaner(self, df):
        """Return the headlines cleaned"""
        df['Headline'] = df['Headline'].str.lstrip()

        return df


    @staticmethod
    def head(df):
        print("\n")
        print(df.head())


    @staticmethod
    def save(df, filename = "data\cleaned_headlines.csv"):
        df.to_csv(filename)

