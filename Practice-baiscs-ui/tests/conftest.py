import pytest
from reusable_codes.chrome_actions import open_chrome

#Adding fixtures
@pytest.fixture
def driver():
    """
    Browser setup and teardown fixture
    """
    driver = open_chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
