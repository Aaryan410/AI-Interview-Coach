import json 
from pathlib import Path


def load_questions(role):
    file_path = Path("questions") / f"{role}.json"

    with open(file_path, "r") as name:
        return json.load(name)