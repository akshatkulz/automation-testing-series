import pytest
import os
from datetime import datetime
from reusable_codes.chrome_actions import open_chrome


@pytest.fixture
def driver(request):
    driver = open_chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    # Take screenshot if test failed
    if request.node.rep_call.failed:
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        screenshot_name = (
            f"{request.node.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )
        driver.save_screenshot(os.path.join(screenshots_dir, screenshot_name))

    driver.quit()


# Hook to check test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
