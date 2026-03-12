import random

from colorama import Fore, Style

MIN_TO_CITY_DISTANCE = 1
MAX_TO_CITY_DISTANCE = 1000
to_city_distance = random.randint(MIN_TO_CITY_DISTANCE, MAX_TO_CITY_DISTANCE)

print(f"Расстояние до города: {to_city_distance} км")

covered_to_city_distance = 0
MIN_PER_DAY_DISTANCE = 1
MAX_PER_DAY_DISTANCE = 100
is_city_found = False

SUCCESSFUL_FINDING_CITY_TEXT_COLOR = Fore.GREEN
UNSUCCESSFUL_FINDING_CITY_TEXT_COLOR = Fore.RED

while covered_to_city_distance < to_city_distance:
    per_day_distance = MIN_PER_DAY_DISTANCE - 1
    per_day_distance_info = ''
    is_per_day_distance_valid = False

    remaining_distance = to_city_distance - covered_to_city_distance
    total_max_per_day_distance = min(MAX_PER_DAY_DISTANCE, remaining_distance)

    while not is_per_day_distance_valid:
        per_day_distance_info = input("Введите расстояние за день. Расстояние должно быть целым числом: ")

        if per_day_distance_info.isdigit():
            per_day_distance = int(per_day_distance_info)
            if MIN_PER_DAY_DISTANCE <= per_day_distance <= total_max_per_day_distance:
                is_per_day_distance_valid = True
            else:
                print(f"Пройденное расстояние должно быть от {MIN_PER_DAY_DISTANCE} до {total_max_per_day_distance}!")
        else:
            print("Введите только целое число")

    covered_to_city_distance += per_day_distance

    print(f"Сегодня вы прошли {per_day_distance}. "
          f"Всего пройдено {covered_to_city_distance} км. Город пока что не найден.")

print(SUCCESSFUL_FINDING_CITY_TEXT_COLOR, end='')
print("Город найден!", end='')
print(Style.RESET_ALL)
