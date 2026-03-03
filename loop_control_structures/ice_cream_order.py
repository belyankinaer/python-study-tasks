BANANA_FLAVOR = "банановый"
APPLE_FLAVOR = "яблочный"
CHERRY_FLAVOR = "вишневый"

TRUE_ANSWER = "да"
FALSE_ANSWER = "нет"

ice_cream_flavors = ""

client_is_finished = False

while not client_is_finished:
    ice_cream_flavor = input(f"Какой вкус мороженого вы хотите? "
                             f"В наличии: {BANANA_FLAVOR}, {APPLE_FLAVOR}, {CHERRY_FLAVOR}.").strip().lower()

    while (ice_cream_flavor != BANANA_FLAVOR
           and ice_cream_flavor != APPLE_FLAVOR
           and ice_cream_flavor != CHERRY_FLAVOR):
        print("Такого вкуса нет в меню.")
        ice_cream_flavor = input(f"В наличии: {BANANA_FLAVOR}, {APPLE_FLAVOR}, {CHERRY_FLAVOR}.").strip().lower()

    if ice_cream_flavors:
        ice_cream_flavors = f"{ice_cream_flavors}, {ice_cream_flavor}"
    else:
        ice_cream_flavors = ice_cream_flavor

    client_answer = input(f"Вы закончили свой выбор? "
                          f"{TRUE_ANSWER.capitalize()}/{FALSE_ANSWER.capitalize()}: ").strip().lower()
    while TRUE_ANSWER != client_answer and FALSE_ANSWER != client_answer:
        client_answer = input(f"{TRUE_ANSWER.capitalize()} или {FALSE_ANSWER.capitalize()}?").strip().lower()

    if client_answer == TRUE_ANSWER:
        client_is_finished = True
    else:
        client_is_finished = False

print("Список ваших вкусов: ", end='')
print(ice_cream_flavors)
