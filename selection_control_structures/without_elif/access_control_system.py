employee_id = int(input("Введите идентификатор сотрудника: "))

ADMIN_ID = 1
OPERATOR_ID = 2
WORKING_DAY_START_TIME = 9
WORKING_DAY_END_TIME = 18

if employee_id == ADMIN_ID:
    print("Доступ разрешен")
else:
    if employee_id == OPERATOR_ID:
        current_time = int(input(f"Введите текущее время (например: {WORKING_DAY_START_TIME}): "))
        if WORKING_DAY_START_TIME <= current_time <= WORKING_DAY_END_TIME:
            print("Доступ разрешен")
        else:
            print("Доступ запрещен")
    else:
        print("Доступ запрещен")
