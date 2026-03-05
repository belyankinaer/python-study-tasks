from datetime import datetime

from colorama import Fore, Style

HIGHLIGHT_COLOR = Fore.BLUE

print(HIGHLIGHT_COLOR, end='')
user_age = int(input("Введите ваш возраст: "))

current_year = datetime.now().year
user_birth_year = current_year - user_age
print("Ваш год рождения:")
print(Style.RESET_ALL, end='')
print(user_birth_year)
