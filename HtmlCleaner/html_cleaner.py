from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import locale

class MyHtmlCleaner:
    headline = []
    date     = []

    def __init__(self):
        pass

    def article_parser(self, page_source, html_class):
        soup = BeautifulSoup(page_source, 'lxml')
        articles_container = soup.find_all('article', class_ = html_class)

        for container in articles_container:
            MyHtmlCleaner.headline.append(container.h2.text)
            MyHtmlCleaner.date.append(container.time.text)

        return pd.DataFrame({'Date': MyHtmlCleaner.date,
                            'Headline': MyHtmlCleaner.headline})

    @staticmethod
    def print_headlines(article_parser):
        return print(article_parser.head() + "\n")

