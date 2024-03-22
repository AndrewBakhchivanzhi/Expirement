class Question:

    def __init__(self, qwestion, difficulty, true_answer, is_question=False, answer=None, count=0):
        self.qwestion = qwestion
        self.difficulty = difficulty
        self.true_answer = true_answer
        self.is_question = is_question
        self.answer = answer
        self.count = count


    def __str__(self):
        return f'{self.qwestion}, {self.difficulty}, {self.true_answer}'

    def __repr__(self):
        return f'Question(qwestion={self.qwestion}, difficulty={self.difficulty}, true_answer={self.true_answer}'

    def get_points(self):
        """Возвращает int, количество баллов"""
        if self.answer == self.true_answer:
            self.count = int(self.difficulty)*10

    def is_correct(self, answer):
        """Возвращает True, если ответ пользователя совпадает с верным ответов иначе False"""
        if answer == self.true_answer:
            return True
        else:
            return False

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде"""
        return f'{self.qwestion}'

    def build_feedback(self):
        """Возвращает верный ответ или нет и колличество балов"""
        if self.answer == self.true_answer:
            return f'Ответ верный, получено {self.difficulty * 10} баллов'
        else:
            return f'Ответ неверный, верный ответ {self.true_answer}'
