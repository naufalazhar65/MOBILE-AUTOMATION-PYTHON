from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

from config.android_config import get_android_capabilities
from config.ios_config import get_ios_capabilities


class DriverFactory:

    @staticmethod
    def create(platform):

        if platform.lower() == "android":

            options = UiAutomator2Options().load_capabilities(
                get_android_capabilities()
            )

        elif platform.lower() == "ios":

            options = XCUITestOptions().load_capabilities(
                get_ios_capabilities()
            )

        else:

            raise ValueError(
                f"Platform '{platform}' is not supported."
            )

        return webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)