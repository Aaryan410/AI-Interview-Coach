import json 

def load_questions(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data