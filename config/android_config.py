from pathlib import Path

# Path APK
APP_PATH = Path(__file__).resolve().parent.parent / "apps" / "MyDemoAppRN.apk"


def get_android_capabilities():
    return {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "Google Pixel 4",
        "appium:platformVersion": "12",
        "appium:udid": "emulator-5554",
        "appium:noReset": False,
        "appium:app": str(APP_PATH),
    }