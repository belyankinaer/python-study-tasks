from colorama import Fore, Style

HIGHLIGHT_COLOR = Fore.BLUE

print(HIGHLIGHT_COLOR, end='')
user_favorite_color = input("Введите ваш любимый цвет: ")
user_favorite_animal = input("Введите ваше любимое животное: ")

print(Style.RESET_ALL, end='')
print("Ваш любимый цвет ")
print(HIGHLIGHT_COLOR, end='')
print(user_favorite_color)
print(Style.RESET_ALL, end='')
print(", а ваше любимое животное ")
print(HIGHLIGHT_COLOR, end='')
print(user_favorite_animal)
