import random

from colorama import Fore, Style

SUCCESSFUL_FINDING_CITY_TEXT_COLOR = Fore.GREEN
UNSUCCESSFUL_FINDING_CITY_TEXT_COLOR = Fore.RED

MIN_TO_CITY_DISTANCE = 1
MAX_TO_CITY_DISTANCE = 1000
to_city_distance = random.randint(MIN_TO_CITY_DISTANCE, MAX_TO_CITY_DISTANCE)

MIN_PER_DAY_DISTANCE = 1
MAX_PER_DAY_DISTANCE = 100

covered_distance = 0
city_found = False

print(f"Расстояние до города: {to_city_distance} км")

while covered_distance < to_city_distance:
    per_day_distance = MIN_PER_DAY_DISTANCE - 1
    is_per_day_distance_valid = False
    per_day_distance_info = ''

    while not is_per_day_distance_valid:
        while per_day_distance_info.isdigit() == False:
            per_day_distance_info = input('Введите расстояние за день. Расстояние должно быть целым числом: ')

        per_day_distance = int(per_day_distance_info)

        if per_day_distance < MIN_PER_DAY_DISTANCE or per_day_distance > MAX_PER_DAY_DISTANCE:
            print('Пройденное расстояние должно быть от 1 до 100!')
        else:
            is_per_day_distance_valid = True

    remaining_distance = to_city_distance - covered_distance

    if per_day_distance > remaining_distance:
        covered_distance += remaining_distance
        print(f"Вы прошли {remaining_distance} км (из {per_day_distance} км) и нашли город. Город найден!")
    else:
        covered_distance += per_day_distance
        if covered_distance >= to_city_distance:
            print(SUCCESSFUL_FINDING_CITY_TEXT_COLOR + 'Город найден!' + Style.RESET_ALL)
            city_found = True
        else:
            print(
                f'Сегодня вы прошли {per_day_distance}. Всего пройдено {covered_distance} км. Город пока что не найден.')
