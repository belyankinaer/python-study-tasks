WARRIOR_CLASS = "Воин"
MAGICIAN_CLASS = "Маг"
OUTLAW_CLASS = "Разбойник"

hero_class = input(f'Выберите класс персонажа: {WARRIOR_CLASS}, {MAGICIAN_CLASS}, {OUTLAW_CLASS}.').strip().capitalize()

if hero_class in [WARRIOR_CLASS, MAGICIAN_CLASS, OUTLAW_CLASS]:
    print("Способности класса персонажа:")
    print("Персонаж умеет", end=" ")
    if hero_class == WARRIOR_CLASS:
        print("сильно атаковать.")
    elif hero_class == MAGICIAN_CLASS:
        print("колдовать.")
    elif hero_class == OUTLAW_CLASS:
        print("воровать.")
else:
    print("Выбран неверный класс.")
