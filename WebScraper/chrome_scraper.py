from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MyChromeWebScraper:

    OPTIONS = webdriver.ChromeOptions()
    OPTIONS.add_argument('--ignore-certificate-errors')
    OPTIONS.add_argument('--incognito')
    OPTIONS.add_argument('--headless')
    driver = webdriver.Chrome('chromedriver.exe', options = OPTIONS)

    def __init__(self):
        pass


    def scrap(self, url, nbr_clicks, xpath):
        i = 0
        MyChromeWebScraper.driver.get(url)

        while i < nbr_clicks:
            try:
                show_more_button = MyChromeWebScraper.driver.find_element_by_xpath(xpath)
                show_more_button.click()
                i += 1
                time.sleep(0.5)
            except Exception as e:
                print (e)
                break

        page_source = MyChromeWebScraper.driver.page_source
        MyChromeWebScraper.driver.quit()
        print('Scrap complete')

        return page_source


    def kill_driver(self):
        MyChromeWebScraper.driver.quit()
