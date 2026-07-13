import json 
from pathlib import Path


def load_questions(role, topic):
    file_path = Path("questions") / Path(role) / f"{topic}.json"
    with open(file_path, "r", encoding = "utf-8") as file:
        return json.load(file)