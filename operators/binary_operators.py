# Демонстрация всех операторов Python для 10 комбинаций типов
# число=int, флоат=float, строка=str, булево=bool

print("=== АРИФМЕТИЧЕСКИЕ ОПЕРАТОРЫ ===\n")

# + (сложение/конкатенация)
print("1) ЧИСЛО + ЧИСЛО: 2 + 3 =", 2 + 3)  # Обычное сложение: 5 [web:11]
print("2) ЧИСЛО + ФЛОАТ: 2 + 3.5 =", 2 + 3.5)  # int преобразуется в float: 5.5 [web:11]
print("3) ЧИСЛО + СТРОКА: 2 + 'ab' =", 2 + 'ab')  # TypeError - разные типы!
print("4) ЧИСЛО + БУЛЕВО: 5 + True =", 5 + True)  # True=1: 6 [web:11]
print("5) СТРОКА + ФЛОАТ: 'ab' + 3.5 =", 'ab' + 3.5)  # TypeError
print("6) СТРОКА + БУЛЕВО: 'ab' + True =", 'ab' + True)  # TypeError
print("7) СТРОКА + СТРОКА: 'ab' + 'cd' =", 'ab' + 'cd')  # Конкатенация: 'abcd' [web:4]
print("8) ФЛОАТ + ФЛОАТ: 1.5 + 2.5 =", 1.5 + 2.5)  # 4.0 [web:11]
print("9) ФЛОАТ + БУЛЕВО: 1.5 + True =", 1.5 + True)  # True=1.0: 2.5 [web:11]
print("10) БУЛЕВО + БУЛЕВО: True + False =", True + False)  # 1+0=1 [web:11]
print()

# - (вычитание)
print("1) 5 - 2 =", 5 - 2)  # 3 [web:11]
print("2) 5 - 2.5 =", 5 - 2.5)  # 2.5 [web:11]
print("3) 5 - 'ab' =", 5 - 'ab')  # TypeError
print("4) 5 - True =", 5 - True)  # 4 [web:11]
print("5) 'ab' - 2.5 =", 'ab' - 2.5)  # TypeError
print("6) 'ab' - True =", 'ab' - True)  # TypeError
print("7) 'ab' - 'cd' =", 'ab' - 'cd')  # TypeError - строки не вычитаются!
print("8) 5.5 - 2.0 =", 5.5 - 2.0)  # 3.5 [web:11]
print("9) 5.5 - True =", 5.5 - True)  # 4.5 [web:11]
print("10) True - False =", True - False)  # 1 [web:11]
print()

# * (умножение/повтор)
print("1) 2 * 3 =", 2 * 3)  # 6 [web:11]
print("2) 2 * 3.5 =", 2 * 3.5)  # 7.0 [web:11]
print("3) 3 * 'ab' =", 3 * 'ab')  # 'ababab' - строка повторяется! [web:9]
print("4) 5 * False =", 5 * False)  # 0 [web:11]
print("5) 'ab' * 3.5 =", 'ab' * 3.5)  # TypeError - только int!
print("6) 'ab' * True =", 'ab' * True)  # 'ab' (True=1) [web:11]
print("7) 'ab' * 'cd' =", 'ab' * 'cd')  # TypeError
print("8) 1.5 * 2.0 =", 1.5 * 2.0)  # 3.0 [web:11]
print("9) 1.5 * False =", 1.5 * False)  # 0.0 [web:11]
print("10) True * True =", True * True)  # 1 [web:11]
print()

# / (деление - всегда float!)
print("1) 5 / 2 =", 5 / 2)  # 2.5 [web:11]
print("2) 5 / 2.0 =", 5 / 2.0)  # 2.5 [web:11]
print("3) 5 / 'ab' =", 5 / 'ab')  # TypeError
print("4) 5 / True =", 5 / True)  # 5.0 [web:11]
print("5) 'ab' / 2.0 =", 'ab' / 2.0)  # TypeError
print("6) 'ab' / True =", 'ab' / True)  # TypeError
print("7) 'ab' / 'cd' =", 'ab' / 'cd')  # TypeError
print("8) 5.0 / 2.0 =", 5.0 / 2.0)  # 2.5 [web:11]
print("9) 5.0 / True =", 5.0 / True)  # 5.0 [web:11]
print("10) True / True =", True / True)  # 1.0 [web:11]
# print("True / False")  # ZeroDivisionError!
print()

# // (целочисленное деление)
print("1) 5 // 2 =", 5 // 2)  # 2 [web:11]
print("2) 5 // 2.0 =", 5 // 2.0)  # 2.0 (float!) [web:11]
print("3) 5 // 'ab' =", 5 // 'ab')  # TypeError
print("4) 5 // True =", 5 // True)  # 5 [web:11]
print("5) 'ab' // 2.0 =", 'ab' // 2.0)  # TypeError
print("6) 'ab' // True =", 'ab' // True)  # TypeError
print("7) 'ab' // 'cd' =", 'ab' // 'cd')  # TypeError
print("8) 5.5 // 2.0 =", 5.5 // 2.0)  # 2.0 [web:11]
print("9) 5.5 // True =", 5.5 // True)  # 5.0 [web:11]
print("10) True // True =", True // True)  # 1 [web:11]
print()

# ** (степень)
print("1) 2 ** 3 =", 2 ** 3)  # 8 [web:3]
print("2) 9 ** 0.5 =", 9 ** 0.5)  # 3.0 (квадратный корень!) [web:3]
print("3) 2 ** 'ab' =", 2 ** 'ab')  # TypeError
print("4) 5 ** True =", 5 ** True)  # 5 (5^1) [web:11]
print("5) 'ab' ** 2.0 =", 'ab' ** 2.0)  # TypeError
print("6) 'ab' ** True =", 'ab' ** True)  # TypeError
print("7) 'ab' ** 'cd' =", 'ab' ** 'cd')  # TypeError
print("8) 4.0 ** 0.5 =", 4.0 ** 0.5)  # 2.0 [web:3]
print("9) 2.5 ** True =", 2.5 ** True)  # 2.5 [web:11]
print("10) False ** False =", False ** False)  # 1 (0^0=1 в Python!) [web:11]
print()

# % (остаток)
print("1) 5 % 2 =", 5 % 2)  # 1 [web:11]
print("2) 5 % 2.0 =", 5 % 2.0)  # 1.0 [web:11]
print("3) 5 % 'ab' =", 5 % 'ab')  # TypeError
print("4) 5 % True =", 5 % True)  # 0 [web:11]
print("5) 'ab' % 2.0 =", 'ab' % 2.0)  # TypeError
print("6) 'ab' % True =", 'ab' % True)  # TypeError
print("7) 'ab' % 'cd' =", 'ab' % 'cd')  # '%s %s' % ('ab', 'cd') = 'ab cd' (форматирование!) [web:4]
print("8) 5.5 % 2.0 =", 5.5 % 2.0)  # 1.5 [web:11]
print("9) 5.5 % True =", 5.5 % True)  # 0.5 [web:11]
print("10) True % True =", True % True)  # 0 [web:11]
print()

print("=== ОПЕРАТОРЫ СРАВНЕНИЯ (все возвращают bool) ===\n")
print("1) ЧИСЛО > ЧИСЛО: 2 > 1 =", 2 > 1)  # True [web:6]
print("2) ЧИСЛО == ФЛОАТ: 2 == 2.0 =", 2 == 2.0)  # True (одинаковое значение!) [web:10]
print("3) ЧИСЛО > СТРОКА: 2 > 'ab' =", 2 > 'ab')  # TypeError в Python 3!
print("4) ЧИСЛО > БУЛЕВО: 2 > True =", 2 > True)  # True (True=1) [web:11]
print("5) СТРОКА > ФЛОАТ: 'ab' > 3.5 =", 'ab' > 3.5)  # TypeError
print("6) СТРОКА > БУЛЕВО: 'ab' > True =", 'ab' > True)  # TypeError
print("7) СТРОКА > СТРОКА: 'ab' < 'b' =", 'ab' < 'b')  # True (лексикографически) [web:4]
print("8) ФЛОАТ < ФЛОАТ: 1.5 < 2.0 =", 1.5 < 2.0)  # True [web:11]
print("9) ФЛОАТ > БУЛЕВО: 1.5 > True =", 1.5 > True)  # True [web:11]
print("10) БУЛЕВО == БУЛЕВО: True == True =", True == True)  # True [web:11]
print()

print("=== ЛОГИЧЕСКИЕ ОПЕРАТОРЫ and/or (возвращают операнд!) ===\n")
print("1) 2 and 3 =", 2 and 3)  # 3 (второй истинный) [web:12]
print("2) 2 and 0.0 =", 2 and 0.0)  # 0.0 (второй ложный) [web:12]
print("3) 1 and 'hi' =", 1 and 'hi')  # 'hi' [web:12]
print("4) 0 or True =", 0 or True)  # True (второй при первом ложном) [web:12]
print("5) '' or 3.5 =", '' or 3.5)  # 3.5 (пустая строка ложная) [web:12]
print("6) 'x' and False =", 'x' and False)  # False [web:12]
print("7) '' or 'b' =", '' or 'b')  # 'b' [web:12]
print("8) 0.0 or 2.5 =", 0.0 or 2.5)  # 2.5 [web:12]
print("9) 1.5 and False =", 1.5 and False)  # False [web:12]
print("10) True or False =", True or False)  # True (первый истинный) [web:12]
print()

print("=== ОПЕРАТОРЫ ПРИСВАИВАНИЯ (изменяют переменную) ===\n")
a = 5
print("a = 5:", a)
a += 3    # a = a + 3
print("a += 3:", a)  # 8 [web:4]
a -= 2    # a = a - 2
print("a -= 2:", a)  # 6 [web:4]
a *= 2    # a = a * 2
print("a *= 2:", a)  # 12 [web:4]
a /= 3    # a = a / 3 (становится float!)
print("a /= 3:", a, type(a))  # 4.0 <class 'float'> [web:4]
a = 5     # сброс
a %= 2
print("a %= 2:", a)  # 1 [web:4]
a = 2
a **= 3
print("a **= 3:", a)  # 8 [web:4]
