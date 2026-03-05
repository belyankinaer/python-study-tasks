result = (5 > 3 and 4 < 7) or not (8 == 9)
print(result)
# операторы and, or, not
# 1) 5 > 3 = True
# 2) 4 < 7 = True
# 3) 8 == 9 = False
# 4) not (8 == 9) = True
# 5) (5 > 3 and 4 < 7) = True and True = True
# 6) (5 > 3 and 4 < 7) or not (8 == 9) = True or True = True

a, b = 5, 7
result = (a > b) if (a > 0 and b > 0) else (a < 0 or b < 0)
print(result)
# операторы and, or
# 1) a > 0 = True
# 2) b > 0 = True
# 3) (a > 0 and b > 0) = True and True = True (тк тут True то условие if выполняется, а else не выполняется)
# 4) a > b = 5 > 7 = False
