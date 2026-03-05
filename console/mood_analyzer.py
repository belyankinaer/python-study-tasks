from colorama import Fore

HAPPINESS_TEXT_COLOR = Fore.GREEN
SADNESS_TEXT_COLOR = Fore.BLUE
CALM_TEXT_COLOR = Fore.WHITE
ERROR_TEXT_COLOR = Fore.RED

HAPPINESS_MOOD = 'радость'
SADNESS_MOOD = 'грусть'
CALM_MOOD = 'спокойствие'

user_mood = input(f'Введите ваше настроение({HAPPINESS_MOOD}, {SADNESS_MOOD}, {CALM_MOOD}): ').lower().strip()

if user_mood == HAPPINESS_MOOD:
    print(HAPPINESS_TEXT_COLOR + 'Мы рады видеть вас в хорошем настроении!')
elif user_mood == SADNESS_MOOD:
    print(SADNESS_TEXT_COLOR + 'Очень жаль, что вы испытали грусть.')
elif user_mood == CALM_MOOD:
    print(CALM_TEXT_COLOR + 'Очень приятно, что вы спокойны.')
else:
    print(ERROR_TEXT_COLOR + 'Извините, я не знаю такого настроения.')
