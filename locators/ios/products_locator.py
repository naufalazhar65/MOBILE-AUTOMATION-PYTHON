from appium.webdriver.common.appiumby import AppiumBy


class ProductsLocator:

    SORT_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "sort button"
    )

    NAME_ASC = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Name - Ascending"]'
    )

    NAME_DESC = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Name - Descending"]'
    )

    PRICE_ASC = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Price - Ascending"]'
    )

    PRICE_DESC = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Price - Descending"]'
    )

    FIRST_PRODUCT = (
        AppiumBy.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeStaticText[`label == "Sauce Labs Backpack"`]'
    )

    FIRST_PRICE = (
        AppiumBy.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeStaticText[`label == "$7.99"`]'
    )