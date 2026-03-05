FIRST_STRING_NOTE = "ми"
SECOND_STRING_NOTE = "си"
THIRD_STRING_NOTE = "соль"
FOURTH_STRING_NOTE = "ре"
FIFTH_STRING_NOTE = "ля"
SIXTH_STRING_NOTE = "ми"

FIRST_STRING_NUMBER = 1
SECOND_STRING_NUMBER = 2
THIRD_STRING_NUMBER = 3
FOURTH_STRING_NUMBER = 4
FIFTH_STRING_NUMBER = 5
SIXTH_STRING_NUMBER = 6

SPLITTER = " "

string_number = int(input("Номер струны (1-6): "))

if FIRST_STRING_NUMBER <= string_number <= SECOND_STRING_NUMBER:
    print('Правильная настройка на ноту', end=SPLITTER)

    if string_number == FIRST_STRING_NUMBER:
        right_setting = FIRST_STRING_NOTE
    elif string_number == SECOND_STRING_NUMBER:
        right_setting = SECOND_STRING_NOTE
    elif string_number == THIRD_STRING_NUMBER:
        right_setting = THIRD_STRING_NOTE
    elif string_number == FOURTH_STRING_NUMBER:
        right_setting = FOURTH_STRING_NOTE
    elif string_number == FIFTH_STRING_NUMBER:
        right_setting = FIFTH_STRING_NOTE
    else:
        right_setting = SIXTH_STRING_NOTE
    print(f'"{right_setting}"')
else:
    print("Номер струны должен быть от 1 до 6.")
