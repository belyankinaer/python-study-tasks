client_feedback_text = " ваш сервис отличный. очень доволен обслуживанием... "
sentence_spliter = "."

client_feedback_parts = client_feedback_text.split(sentence_spliter)

first_sentence_index = 0
second_sentence_index = 1
first_sentence = client_feedback_parts[first_sentence_index].strip().capitalize()
second_sentence = client_feedback_parts[second_sentence_index].strip().capitalize()

print(f"{first_sentence}.")
print(f"{second_sentence}.")
