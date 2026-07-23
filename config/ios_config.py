from appium.options.ios import XCUITestOptions

options = XCUITestOptions()

options.platform_name = "iOS"
options.set_capability("automationName", "XCUITest")
options.set_capability("deviceName", "iPhone 17 Pro")
options.set_capability("platformVersion", "26.4")
options.set_capability("udid", "3293AF1E-3396-4D4C-873B-9FD3B6E73E53")
options.set_capability("bundleId", "com.saucelabs.mydemo.app.ios")
options.set_capability("noReset", True)