
from selenium.webdriver.common.by import By
import time

class Parser_SN:
    def parsing_Secure_news(self,browser_SN):
        browser_SN.get('https://securenews.ru/news/')
        time.sleep(0.5)
        browser_SN.execute_script("window.scrollTo(0, 2000)")
        self.news_title = browser_SN.find_elements(By.CLASS_NAME, 'post-title')
        self.image = browser_SN.find_elements(By.TAG_NAME, 'img')
        self.href = browser_SN.find_elements(By.LINK_TEXT, "Читать далее")
        self.text_mini = browser_SN.find_elements(By.CLASS_NAME, 'excerpt')

class Parser_AM:
    def parsing_AM(self,browser_SL):
        browser_SL.get('https://www.anti-malware.ru/news')
        self.image = browser_SL.find_elements(By.CLASS_NAME, 'img-responsive')
        self.news_title = browser_SL.find_elements(By.TAG_NAME, 'h2')
        self.href = browser_SL.find_elements(By.TAG_NAME, 'a')
        self.text_mini = browser_SL.find_elements(By.TAG_NAME, 'p')

class Parser_RBC:
    def parsing_RBC(self,browser_RBC):
        browser_RBC.get('https://www.rbc.ru/tags/?tag=информационная%20безопасность')
        self.news_title = browser_RBC.find_elements(By.CLASS_NAME, 'search-item__title')
        self.image = browser_RBC.find_elements(By.CLASS_NAME, 'search-item__image')
        self.href = browser_RBC.find_elements(By.CLASS_NAME, 'search-item__link')
        self.text_mini = browser_RBC.find_elements(By.CLASS_NAME, 'search-item__text')
        self.time = browser_RBC.find_elements(By.CLASS_NAME, 'search-item__category')

RBC_News = Parser_RBC()
Secure_News = Parser_SN()
ANTI_MALWARE = Parser_AM()