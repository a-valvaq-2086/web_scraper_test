from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, "en_US")

class MyHtmlCleaner:
    headline = []
    date     = []


    def __init__(self):
        pass


    def article_parser(self, page_source, html_class):
        """HTML parser for the scraped data. Return a pandas DataFrame with the Dates and the News Headlines."""
        soup = BeautifulSoup(page_source, 'lxml')
        articles_container = soup.find_all('article', class_ = html_class)

        for container in articles_container:
            MyHtmlCleaner.headline.append(container.h2.text)
            MyHtmlCleaner.date.append(container.time.text)

        return pd.DataFrame({'Date': MyHtmlCleaner.date,
                            'Headline': MyHtmlCleaner.headline})

    @staticmethod
    def print_headlines(article_parser):
        """Return the head of the DataFrames containing the articles that BeautifulSoup parsed."""
        return print(article_parser.head() + "\n")


    def date_cleaner(self, article_parser):
        "Return the headlines dates as a Python date object in ISO format"
        
        d_months = {"Jan.": "January", "Feb.": "February", "Aug.": "August", "Sept.": "September",
         "Oct.": "October", "Nov.": "November", "Dec.": "December"}

        for key, val in d_months.items():
            article_parser['Date'] = article_parser['Date'].str.replace(key, val, regex=True)

        article_parser['Date'] = pd.to_datetime(article_parser['Date'], format="%B %d, %Y")

        return article_parser


    def headline_cleaner(self, article_parser):
        """Return the headlines cleaned"""
        article_parser['Headline'] = article_parser['Headline'].str.lstrip()

        return article_parser

    @staticmethod
    def save(article_parser, filename):
        article_parser.to_csv(filename)

