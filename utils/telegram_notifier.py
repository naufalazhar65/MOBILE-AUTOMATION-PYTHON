import os

import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_telegram_message(message, thread_id=None):

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
    }

    if thread_id is not None:
        payload["message_thread_id"] = thread_id

    response = requests.post(
        f"{BASE_URL}/sendMessage",
        data=payload,
        timeout=30,
    )

    # print("=" * 60)
    # print("PAYLOAD")
    # print(payload)
    # print("=" * 60)
    # print("STATUS :", response.status_code)
    # print("BODY   :", response.text)
    # print("=" * 60)

    return

    response.raise_for_status()


def send_telegram_photo(photo_path, caption="", thread_id=None):
    """
    Send Telegram photo.
    """

    payload = {
        "chat_id": CHAT_ID,
        "caption": caption,
        "parse_mode": "HTML",
    }

    if thread_id is not None:
        payload["message_thread_id"] = thread_id

    with open(photo_path, "rb") as photo:

        response = requests.post(
            f"{BASE_URL}/sendPhoto",
            data=payload,
            files={
                "photo": photo,
            },
            timeout=30,
        )

    response.raise_for_status()
    
