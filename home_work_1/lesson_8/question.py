class Question:

    def __init__(self, text, difficulty, correct_answer):
        self.text = text
        self.difficulty = int(difficulty)
        self.correct_answer = correct_answer

        self.is_asked = False
        self.user_answer = None
        self.points = self.difficulty * 10

    def __repr__(self):
        return f"\
            \nВопрос: {self.text}\
            \nСложность: {self.difficulty}/5\
            \nВерный ответ: {self.correct_answer}\
            \nЗадан ли вопрос: {self.is_asked}\
            \nОтвет пользователя: {self.user_answer}\
            \nБаллы за вопрос: {self.points}"

    def get_points(self):
        return self.points

    def is_correct(self):
        return self.user_answer == self.correct_answer

    def build_question(self):
        return f"Вопрос: {self.text}"

    def build_positive(self):
        return f"Да!"

    def build_negative(self):
        return f"Нет!"