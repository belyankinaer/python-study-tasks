EXIT_PROGRAM_WORD = "стоп"

POSITIVE_ANSWER = "да"
NEGATIVE_ANSWER = "нет"

visitor_count = 0

is_program_running = True

while is_program_running:
    is_new_visitor = ''

    while not is_new_visitor == POSITIVE_ANSWER and not is_new_visitor == NEGATIVE_ANSWER:
        is_new_visitor = input("Новый посетитель зашел?").strip().lower()

    if is_new_visitor == POSITIVE_ANSWER:
        visitor_count += 1

    is_program_running = input(f"Вы хотите закончить подсчет? Если да напишите '{EXIT_PROGRAM_WORD}'")
    if is_program_running == EXIT_PROGRAM_WORD:
        is_program_running = False

print(f"Количество новых посетителей за день:", visitor_count)
