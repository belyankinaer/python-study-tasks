full_name = 'Мило Ярослав Леонидович'
splitter = ' '

first_space_index = full_name.index(splitter)
second_space_index = full_name.index(splitter, first_space_index + 1)

surname = full_name[:first_space_index]
print(surname)
name = full_name[first_space_index + 1:second_space_index]
print(name)
patronymic = full_name[second_space_index + 1:]
print(patronymic)
