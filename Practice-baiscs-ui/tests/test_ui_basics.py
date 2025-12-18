from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from reusable_codes.chrome_actions import open_chrome

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