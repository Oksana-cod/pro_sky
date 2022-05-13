import json
from question import Question

PATH = "questions.json"


def load_data(path=PATH):
    with open(path, "r", encoding="utf8") as file:
        return json.load(file)


def load_questions(path=PATH):

    questions_data = load_data(path)

    questions = []

    for question_data in questions_data:
        question = Question(
            question_data["q"],
            question_data["d"],
            question_data["a"],
         )
        questions.append(question)

    return questions


