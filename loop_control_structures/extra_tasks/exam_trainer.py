# Задача “Подготовка к экзамену”
# Вы готовитесь к экзамену , решая примеры по математике. Каждый раз, когда вы решаете
# пример, программа определяет , правильно ли вы его решили. Программа также должна
# следить за количеством правильных и неправильных ответов. Этот процесс продолжается
# до тех пор, пока вы не решите закончить сессию, введя "конец"
# . По завершении
# программа должна показать процент правильных ответов
import random

OPERATORS_INFO = "+ * -"
STOP_SESSION_WORD = "конец"

operators = OPERATORS_INFO.split()
is_session_available = True

user_right_answer_count = 0
user_wrong_answer_count = 0

while is_session_available:
    user_answer_info = ''

    random_operator = random.choice(operators)
    random_first_variable = random.randint(1, 10)
    random_second_variable = random.randint(1, 10)

    if random_operator == "+":
        right_answer = random_first_variable + random_second_variable
    elif random_operator == "-":
        right_answer = random_first_variable - random_second_variable
    else:
        right_answer = random_first_variable * random_second_variable

    print(f"Задача: {random_first_variable} {random_operator} {random_second_variable}")

    while not user_answer_info.lstrip('-').isdigit():
        user_answer_info = input(f"Введите ответ:").strip()

    user_answer = int(user_answer_info)

    if user_answer == right_answer:
        user_right_answer_count += 1
        print('Правильный ответ')
    else:
        user_wrong_answer_count += 1
        print('Неправильный ответ')

    is_user_continue = input(f'Если вы хотите закончить введите слово "{STOP_SESSION_WORD}".').lower().strip()
    if is_user_continue == STOP_SESSION_WORD:
        is_session_available = False

print("Ваши результаты:")
print(f"Количество правильных ответов: {user_right_answer_count}")
print(f"Количество неправильных ответов: {user_wrong_answer_count}")
