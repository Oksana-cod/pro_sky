import random

import utils

def main():

    questions = utils.load_questions()
    random.shuffle(questions)

    for question in questions:
        print(question.build_question())

        answer = input()

        question.user_answer = answer

        if question.is_correct():
            print("Ответ верный")
        else:
            print("Ответ НЕверный")

    stats_correct, stats_points = 0, 0

    for question in questions:
        if question.is_correct():
            stats_correct += 1
            stats_points += question.get_points()

    print(f"Верно отвечено: {stats_correct} Набрано баллов {stats_points} ")


if __name__ == '__main__':
    main()