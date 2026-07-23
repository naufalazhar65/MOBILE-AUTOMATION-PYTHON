from appium.webdriver.common.appiumby import AppiumBy


class LoginLocator:

    USERNAME = (
        AppiumBy.ACCESSIBILITY_ID,
        "Username input field"
    )

    PASSWORD = (
        AppiumBy.ACCESSIBILITY_ID,
        "Password input field"
    )

    LOGIN_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Login button"
    )

    PRODUCTS_TITLE = (
        AppiumBy.ACCESSIBILITY_ID,
        "Products"
    )