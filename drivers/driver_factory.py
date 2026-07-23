from appium import webdriver

from config.android_config import get_android_options
from config.ios_config import get_ios_options


class DriverFactory:

    @staticmethod
    def create(platform):

        if platform.lower() == "android":
            options = get_android_options()

        elif platform.lower() == "ios":
            options = get_ios_options()

        else:
            raise ValueError(
                f"Platform '{platform}' is not supported."
            )

        return webdriver.Remote(
            "http://127.0.0.1:4723",
            options=options,
        )