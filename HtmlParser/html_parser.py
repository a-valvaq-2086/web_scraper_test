from bs4 import BeautifulSoup
import pandas as pd


class MyHtmlParser:
    headline = []
    date     = []


    def __init__(self):
        pass


    def article_parser(self, page_source, html_class):
        """HTML parser for the scraped data. Return a pandas DataFrame with the Dates and the News Headlines."""
        soup = BeautifulSoup(page_source, 'lxml')
        articles_container = soup.find_all('article', class_ = html_class)

        for container in articles_container:
            MyHtmlParser.headline.append(container.h2.text)
            MyHtmlParser.date.append(container.time.text)

        return pd.DataFrame({'Date': MyHtmlParser.date,
                            'Headline': MyHtmlParser.headline})


    @staticmethod
    def print_headlines(article_parser):
        """Return the head of the DataFrames containing the articles that BeautifulSoup parsed."""
        return print(article_parser.head() + "\n")