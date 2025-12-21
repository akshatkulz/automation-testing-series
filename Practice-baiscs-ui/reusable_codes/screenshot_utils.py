import os
from datetime import datetime


def take_screenshot(driver, test_name, step_name):
    """
    Screenshot name format:
    testname_step_timestamp.png
    """
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{test_name}_{step_name}_{timestamp}.png"

    driver.save_screenshot(os.path.join(screenshots_dir, file_name))
