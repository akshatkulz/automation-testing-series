from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePage:
    """
    Page Object for Google Search Page
    """

    SEARCH_BOX = (By.NAME, "q")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.google.com")

    def search(self, text):
        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )
        search_box.send_keys(text)
        search_box.submit()

    def get_title(self):
        return self.driver.title
