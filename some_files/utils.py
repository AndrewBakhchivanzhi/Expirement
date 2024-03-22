
def write_files(file_to_write):

    user_language = input("Какой язык вы учите ")
    user_time = input("Как давно? ")
    user_institution = input("Где? ")

    with open(file_to_write, "w+", encoding='UTF-8') as file:
        file.write(f"{user_language}\n")
        file.write(f"{user_time}\n")
        file.write(f"{user_institution}\n")
        print("Ответы записаны")
        file.seek(0)
        print()
        answers_first, answers_second, answers_third = file.readlines()
        answers_first = answers_first.rstrip('\n')
        answers_second = answers_second.rstrip('\n')
        answers_third = answers_third.rstrip('\n')
        print(f"Вы учите язык {answers_first} {answers_second} в {answers_third}")


def word_check(file):

    search_word = input("Какое слово хотим проверить? ")

    with open(file, 'rt', encoding='UTF-8') as file:
        content = file.read()

        if search_word in content:
            print("Слово обнаружено")
        else:
            print("Таких слов нет")


def enter_a_word(file):
    new_word = input("Какое слово хотим добавить? ")

    with open(file, 'a', encoding='UTF-8') as file:
        file.write(f"\n{new_word}\n")