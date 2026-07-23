import os
import pytest

from drivers.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="android | ios"
    )


@pytest.fixture(scope="function")
def driver(request):

    platform = request.config.getoption("--platform")

    driver = DriverFactory.create(platform)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("reports/screenshots", exist_ok=True)

            driver.save_screenshot(
                f"reports/screenshots/{item.name}.png"
            )