import os
from datetime import datetime


def take_screenshot(driver, test_name):

    screenshot_directory = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "screenshots"
    )

    screenshot_directory = os.path.abspath(screenshot_directory)

    os.makedirs(screenshot_directory, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"{test_name}_{timestamp}.png"

    file_path = os.path.join(screenshot_directory, file_name)

    driver.save_screenshot(file_path)

    return file_path
