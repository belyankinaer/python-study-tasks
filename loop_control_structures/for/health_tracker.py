WEEK_DAYS_COUNT = 7

SMALL_ACTIVITY_STEPS_COUNT = 5000
HIGH_ACTIVITY_STEPS_COUNT = 10000

SMALL_ACTIVITY_ADVICE_TEXT = "Недостаточно активности"
MEDIUM_ACTIVITY_ADVICE_TEXT = "Нормальная активность"
HIGH_ADVICE_TEXT = "Высокая активность"

per_week_steps_info = ""

user_info = ''
for day_number in range(1, WEEK_DAYS_COUNT + 1):

    while not user_info.isdigit() or int(user_info) < 0:
        user_info = input(f"Введите количество шагов за день №:{day_number}")
    per_day_steps_count = int(user_info)
    user_info = ''
    per_week_steps_info += f"{per_day_steps_count} "

total_week_steps_count = 0

for day_count in per_week_steps_info.split():
    total_week_steps_count += int(day_count)

average_per_day_steps_count = total_week_steps_count / WEEK_DAYS_COUNT

print(f"Среднее количество шагов за день: {average_per_day_steps_count}.", end=' ')

if average_per_day_steps_count < SMALL_ACTIVITY_STEPS_COUNT:
    print(f"{SMALL_ACTIVITY_ADVICE_TEXT}.")
elif SMALL_ACTIVITY_STEPS_COUNT <= average_per_day_steps_count < HIGH_ACTIVITY_STEPS_COUNT:
    print(f"{MEDIUM_ACTIVITY_ADVICE_TEXT}.")
elif average_per_day_steps_count >= HIGH_ACTIVITY_STEPS_COUNT:
    print(f"{HIGH_ADVICE_TEXT}.")
