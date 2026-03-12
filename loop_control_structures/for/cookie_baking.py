COOKIE_PER_MINUTE_COUNT = 10
ONE_COOKIE_SYMBOL = "*"

user_info = ""

while not user_info.isdigit() or int(user_info) < 0:
    user_info = input("Введите время работы печи в минутах:")

working_oven_time = int(user_info)

print("Итого печь испекла:")
for minute in range(0, working_oven_time):
    print(ONE_COOKIE_SYMBOL * COOKIE_PER_MINUTE_COUNT)
