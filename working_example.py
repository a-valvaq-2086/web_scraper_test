from WebScraper import MyChromeWebScraper
import sys

url   = "https://www.nytimes.com/topic/company/boeing-company"
XPATH = "//*[@id='latest-panel']/div[1]/div/div/button"

while True:
    try:
        driver = MyChromeWebScraper()
        print(driver.scrap(url, 20, XPATH))
    except	KeyboardInterrupt:
        print("Goodbye")
        driver.kill_driver()
        sys.exit()