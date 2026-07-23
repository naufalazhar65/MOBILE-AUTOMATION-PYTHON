from pages.login_page import LoginPage
from utils.helpers import load_json


def test_login(driver):

    # Load test data
    data = load_json("test_data/login.json")
    user = data["valid_user"]

    # Buat object LoginPage
    login = LoginPage(driver)

    # Login
    login.login(
        user["username"],
        user["password"]
    )

    # Verifikasi
    assert login.is_login_success()