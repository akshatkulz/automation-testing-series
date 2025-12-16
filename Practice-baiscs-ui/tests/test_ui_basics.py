from reusable_codes.chrome_actions import open_chrome

def test_TC1_maximize_chrome_window():
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
    
def test_TC2_maximize_chrome_window():
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