import argparse
import json
import os
import platform
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from utils.telegram_notifier import (
    send_telegram_message,
    send_telegram_photo,
)

REPORT_PATH = ROOT_DIR / "reports/json/output.json"
SCREENSHOT_DIR = ROOT_DIR / "reports/screenshots"


def run_tests(target_platform="android"):
    """
    Run pytest and generate JSON report.
    """

    command = [
        "pytest",
        "--json-report",
        "--json-report-file=reports/json/output.json",
    ]

    if target_platform == "android":
        command.append("tests/android")

    elif target_platform == "ios":
        command.append("tests/ios")

    result = subprocess.run(command)

    return result.returncode


def get_latest_screenshot():

    screenshots = list(SCREENSHOT_DIR.glob("*.png"))

    if not screenshots:
        return None

    return max(
        screenshots,
        key=lambda file: file.stat().st_mtime
    )


def load_report():

    if not REPORT_PATH.exists():
        raise FileNotFoundError("JSON report not found.")

    with open(REPORT_PATH, "r") as file:
        return json.load(file)


def create_summary(report):

    tests = report.get("tests", [])

    passed = 0
    failed = 0
    errors = 0
    skipped = 0

    failed_tests = []

    for test in tests:

        outcome = test.get("outcome")

        if outcome == "passed":
            passed += 1

        elif outcome == "failed":
            failed += 1
            failed_tests.append(test["nodeid"])

        elif outcome == "error":
            errors += 1
            failed_tests.append(test["nodeid"])

        elif outcome == "skipped":
            skipped += 1

    duration = round(report.get("duration", 0), 2)

    return {
        "passed": passed,
        "failed": failed,
        "errors": errors,
        "skipped": skipped,
        "total": len(tests),
        "duration": duration,
        "failed_tests": failed_tests,
    }


def send_summary(summary, target_platform):

    total_failed = summary["failed"] + summary["errors"]

    status = "✅ PASSED" if total_failed == 0 else "❌ FAILED"

    if target_platform == "android":
        device = "Google Pixel 4"
        automation = "UiAutomator2"
    else:
        device = "iPhone 17 Pro"
        automation = "XCUITest"

    branch = os.getenv("GITHUB_REF_NAME", "local")
    commit = os.getenv("GITHUB_SHA", "local")[:7]
    actor = os.getenv("GITHUB_ACTOR", os.getenv("USER", "Unknown"))

    repo = os.getenv("GITHUB_REPOSITORY")
    run_id = os.getenv("GITHUB_RUN_ID")

    if repo and run_id:
        run_url = f"https://github.com/{repo}/actions/runs/{run_id}"
    else:
        run_url = "Running locally"

    failed_section = ""

    if summary["failed_tests"]:

        failed_section = "\n\n❌ Failed Test(s)\n"

        for test in summary["failed_tests"]:
            failed_section += f"• {test}\n"

    message = f"""
📱 <b>Selenium Python Mobile Automation</b>

━━━━━━━━━━━━━━━━━━━━━━

<b>{status}</b>

━━━━━━━━━━━━━━━━━━━━━━

📱 Platform   : {target_platform.capitalize()}
📲 Device     : {device}
🤖 Automation : {automation}
🐍 Python     : {platform.python_version()}
📦 Appium     : 2.x

━━━━━━━━━━━━━━━━━━━━━━

📊 <b>TEST SUMMARY</b>

✅ Passed   : {summary["passed"]}
❌ Failed   : {summary["failed"]}
🔥 Errors   : {summary["errors"]}
⏭️ Skipped : {summary["skipped"]}
📝 Total    : {summary["total"]}
⏱ Duration : {summary["duration"]} s

━━━━━━━━━━━━━━━━━━━━━━

🌿 Branch : {branch}
📝 Commit : {commit}
👤 Actor  : {actor}

━━━━━━━━━━━━━━━━━━━━━━

🔗 {run_url}
{failed_section}
━━━━━━━━━━━━━━━━━━━━━━

🕒 {datetime.now().strftime("%d %b %Y %H:%M")}
"""

    send_telegram_message(message)

    if total_failed > 0:

        screenshot = get_latest_screenshot()

        if screenshot:
            send_telegram_photo(
                screenshot,
                caption="📸 Failure Screenshot",
            )


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--platform",
        choices=["android", "ios"],
        default="android",
        help="Choose platform to execute.",
    )

    args = parser.parse_args()

    exit_code = run_tests(args.platform)

    report = load_report()

    summary = create_summary(report)

    send_summary(summary, args.platform)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()