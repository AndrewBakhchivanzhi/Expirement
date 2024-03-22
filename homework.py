from classes import Question
import json
from random import shuffle

questions = []

with open('qwestion.json', 'r', encoding='UTF-8') as file:
    content = json.load(file)
    for question in content:
        questions.append(Question(question['q'], question['d'], question['a']))


shuffle(questions)
count = 0

def questions(questions):
    for qwestion in questions:
        print(qwestion.build_question())
        user_answer = input("Ваш ответ ")
        if qwestion.is_correct(user_answer):
            print(f'Ответ верный, получено {int(qwestion.difficulty) * 10} баллов')
        else:
            print(f'Ответ неверный. Верный ответ – {qwestion.true_answer}')