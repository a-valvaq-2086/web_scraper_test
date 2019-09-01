from WebScraper import MyChromeWebScraper
from HtmlParser import MyHtmlParser
from DataFrameCleaner import MyDataFrameCleaner
import sys 

"""This is the minimum working example for my news headline web scraper"""

def call_scraper(url, XPATH, nbr_clicks):
    """Simply calls the Chrome Driver to Scrape the desired web
    
    :Args:
         - url: the desired url to scrap content from
         - XPATH: the xpath of the html structure you want to get the info from.
           In this case the location of the Headlines within the webpage.
    """
    while True:
        try:
            driver = MyChromeWebScraper()
            return driver.scrap(url, XPATH, nbr_clicks)
        except	KeyboardInterrupt:
            print("Goodbye")
            driver.kill_driver()
            sys.exit()


def call_parser(page_source, html_class_id):
    """Call the HTML Parser class that uses BeautifulSoup to extract information from the scrapped web"""
    df_headlines = MyHtmlParser()
    return df_headlines.article_parser(page_source, html_class_id)


def call_cleaner(df, file_path_name):
    my_headline = MyDataFrameCleaner(df)
    my_headline.date_cleaner(df)
    my_headline.headline_cleaner(df)
    my_headline.head(df)
    my_headline.save(df, file_path_name)


def main():
    """Entry point"""
    # Scrape the Boeing section of the NYTimes
    url   = "https://www.nytimes.com/topic/company/boeing-company"
    XPATH = "//*[@id='latest-panel']/div[1]/div/div/button"

    page_source  = call_scraper(url, XPATH, 20)
    df_headlines = call_parser(page_source, 'story theme-summary')
    call_cleaner(df_headlines, 'cleaned_headlines.csv')


if __name__ == "__main__":
    main()

