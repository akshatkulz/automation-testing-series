from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from reusable_codes.chrome_actions import open_chrome
from pages.google_page import GooglePage
from reusable_codes.logger import get_logger


def test_TC1_maximize_chrome_window(driver):
    assert driver is not None, "Chrome driver is not intialized"
    """
    # Test Case 1: Open and maximize Chrome browser
    driver = None
    try:
        driver = open_chrome()
        driver.maximize_window()
        assert driver is not None, "Failed to open Chrome Browser"
    
    except Exception as e:
        raise AssertionError(
            f"Test failed while opening or maximizing Chrome. "
            f"Details: {e}"
        )
    """
    
def test_TC2_maximize_chrome_window(driver):
    driver.get("https://www.google.com")
    assert driver.title

    """
    #Test Case 2: Open website and collect title
    driver = None
    try:
        driver = open_chrome()
        driver.maximize_window()
        driver.get("https://www.google.com")

        title = driver.title
        print(f"Website title: {title}")

        # Assert that title is not empty
        assert title, "Page title is empty — page may not have loaded"

    except Exception as e:
        raise AssertionError(
            f"Test failed while collecting website title. Details: {e}"
        )
    """

def test_google_search_title(driver):
    """
    Day 4 TC: Search in Google and validate title
    """
    driver.get("https://www.google.com")

    wait = WebDriverWait(driver, 10)

    # Wait for search box to be visible
    search_box = wait.until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )

    search_box.send_keys("Selenium Python")
    search_box.submit()

    # Wait until title changes
    wait.until(EC.title_contains("Selenium"))

    assert "Selenium" in driver.title, "Search result page not loaded"

    def test_google_search_using_pom(driver):
        """
        Day 5 TC: Google search using Page Object Model
        """
        google_page = GooglePage(driver)

        google_page.open()
        google_page.search("Selenium Python")

        assert "Selenium" in google_page.get_title(), "Search failed"
#Day 6
logger = get_logger(__name__)
def test_google_search_using_pom(driver):
        """
        Day 6 TC: Google search using Page Object Model and logging storing screenshots
        """
        logger.info("Opening Google page")

        google_page = GooglePage(driver)
        google_page.open()

        logger.info("Searching for Selenium Python")
        google_page.search("Selenium Python")

        title = google_page.get_title()
        logger.info(f"Page title after search: {title}")

        assert "Selenium" in title, "Search result title mismatch"
#random
#random 2