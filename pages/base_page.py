from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        logger.info(f"Click element: {locator}")
        self.find(locator).click()

    def type(self, locator, text):
        logger.info(f"Type '{text}' into element: {locator}")
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def is_displayed(self, locator):
        logger.info(f"Verify element is displayed: {locator}")
        return self.find(locator).is_displayed()