client_feedback_text = " ваш сервис отличный. очень доволен обслуживанием... "
cleaned_client_feedback_text = client_feedback_text.strip()
sentence_spliter_index = cleaned_client_feedback_text.find(".")

first_sentence = cleaned_client_feedback_text[:sentence_spliter_index + 1]
first_sentence = first_sentence.strip()
first_sentence = first_sentence.capitalize()

second_sentence = cleaned_client_feedback_text[sentence_spliter_index + 1:]
second_sentence = second_sentence.strip()
second_sentence = second_sentence.capitalize()
sentence_spliter_index = second_sentence.find(".")
second_sentence = second_sentence[:sentence_spliter_index + 1]

# ---

user_name = " ИвАн   "
user_name = user_name.strip()
user_name = user_name.title()
print(user_name)

user_surname = "     ИвАнов"
user_surname = user_surname.strip()
user_surname = user_surname.title()
print(user_surname)

# ---

logs = '2025-11-28 15:44:23 Пользователь ввел неправильный пароль'
first_spliter_index = logs.find(" ")
date = logs[:first_spliter_index]
second_spliter_index = logs.find(" ", first_spliter_index + 1)
time = logs[first_spliter_index + 1:second_spliter_index]
event_info = logs[second_spliter_index + 1:]
print(f"Дата: {date}, Время: {time}, Событие: {event_info}")

# --

advertising_text = 'Не пропустите наше ограниченное предложение на новые модели!'
rewritten_text = advertising_text.replace('ограниченное предложение', 'эксклюзивное предложение')
print(rewritten_text)
