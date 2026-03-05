upper_symbol = 'F'

first_unicode_lower_character = 'a'
first_unicode_upper_character = 'A'
first_lower_character_code = ord(first_unicode_lower_character)
first_upper_character_code = ord(first_unicode_upper_character)
unicode_case_difference = first_lower_character_code - first_upper_character_code

upper_symbol_code = ord(upper_symbol)

lower_symbol_unicode_code = upper_symbol_code + unicode_case_difference
lower_symbol = chr(lower_symbol_unicode_code)

print(lower_symbol)
