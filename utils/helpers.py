from pathlib import Path
import json


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_json(relative_path):
    file_path = PROJECT_ROOT / relative_path

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)