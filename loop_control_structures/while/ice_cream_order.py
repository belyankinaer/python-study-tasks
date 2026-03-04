BANANA_FLAVOR = "банановый"
APPLE_FLAVOR = "яблочный"
CHERRY_FLAVOR = "вишневый"

TRUE_ANSWER = "да"
FALSE_ANSWER = "нет"

ice_cream_flavors = ""

is_client_finished = False

while not is_client_finished:
    ice_cream_flavor = None

while (ice_cream_flavor != BANANA_FLAVOR
       and ice_cream_flavor != APPLE_FLAVOR
       and ice_cream_flavor != CHERRY_FLAVOR):
    print("Такого вкуса нет в меню.")
ice_cream_flavor = input(f"В наличии: {BANANA_FLAVOR}, {APPLE_FLAVOR}, {CHERRY_FLAVOR}.").strip().lower()

ice_cream_flavors += ice_cream_flavor + ','

client_answer = None

while client_answer != TRUE_ANSWER and client_answer != FALSE_ANSWER:
    client_answer = input(f"{TRUE_ANSWER.capitalize()} или {FALSE_ANSWER.capitalize()}?").strip().lower()

if client_answer == TRUE_ANSWER:
    client_is_finished = True

print("Список ваших вкусов: ", end='')
print(ice_cream_flavors)
