import os

from colorama import Fore

GREETING = 'Добро пожаловать в систему'

print(Fore.GREEN, end='')
print("Добрый день, система приветствует Вас!")
input('Нажмите любую клавишу для продолжения...')

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

user_name = input(Fore.BLUE + 'Введите ваше имя: ')
print(Fore.GREEN, end='')
print(f"{GREETING} {user_name}!")
