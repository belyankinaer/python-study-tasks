lower_symbol = 'f'

first_unicode_lower_character = 'a'
first_unicode_upper_character = 'A'
first_lower_character_code = ord(first_unicode_lower_character)
first_upper_character_code = ord(first_unicode_upper_character)
unicode_case_difference = first_lower_character_code - first_upper_character_code

lower_symbol_code = ord(lower_symbol)

upper_symbol_unicode_code = lower_symbol_code - unicode_case_difference
upper_symbol = chr(upper_symbol_unicode_code)

print(upper_symbol)
