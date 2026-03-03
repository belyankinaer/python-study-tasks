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

    while not is_per_day_distance_valid:
        try:
            per_day_distance = int(input('Введите расстояние за день: '))
            if per_day_distance < MIN_PER_DAY_DISTANCE or per_day_distance > MAX_PER_DAY_DISTANCE:
                print('Пройденное расстояние должно быть от 1 до 100!')
            else:
                is_per_day_distance_valid = True
        except ValueError:
            print('Введите целое число!')

    covered_distance += per_day_distance

    if covered_distance >= to_city_distance:
        print(SUCCESSFUL_FINDING_CITY_TEXT_COLOR + 'Город найден!' + Style.RESET_ALL)
        city_found = True
        break
    else:
        print(f'Пройдено {covered_distance} км. Город пока что не найден.')

