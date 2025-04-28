from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class mercadolibreSearch(BasePage):
    SEARCH_FIELD = (By.XPATH, '/html/body/header/div/div[2]/form/input')
    SEARCH_BUTTON = (By.CLASS_NAME, 'nav-search-btn')
    
   
    

    def search(self, search):
        self.enter_text(self.SEARCH_FIELD, 'iphone 13')
        self.click(self.SEARCH_BUTTON)


class searchIphone(BasePage):
    RESULT_SEARCH = (By.XPATH, '/html/body/main/div/div[2]/section')


    def isElementPresent(self):
        elemento = self.find_element(self.RESULT_SEARCH)
        texto = elemento.text
        return texto


