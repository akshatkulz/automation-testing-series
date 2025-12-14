from reusable_codes.chrome_actions import open_chrome

def test_TC1_maximize_chrome_window():
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
    
    finally:
        if driver:
            driver.quit()
