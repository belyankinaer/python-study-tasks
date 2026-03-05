logs = '2025-11-28|15:44:23|Пользователь ввел неправильный пароль'
splitter = '|'
logs_parts = logs.split(splitter)

date_index = 0
time_index = 1
event_info_index = 2

date = logs_parts[date_index]
time = logs_parts[time_index]
event_info = logs_parts[event_info_index]

print(f"Дата: {date}, Время: {time}, Событие: {event_info}")
