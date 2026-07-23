from pathlib import Path

from appium.options.android import UiAutomator2Options

APP_PATH = Path(__file__).resolve().parent.parent / "apps" / "MyDemoAppRN.apk"


def get_android_options():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("deviceName", "Google Pixel 4")
    options.set_capability("platformVersion", "12")
    options.set_capability("udid", "emulator-5554")
    options.set_capability("noReset", False)
    options.set_capability("app", str(APP_PATH))

    return options