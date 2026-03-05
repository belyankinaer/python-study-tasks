MAX_BILL_SUM_WITHOUT_TIP = 500
sum_bill = int(input("Введите сумму счета: "))

if sum_bill > MAX_BILL_SUM_WITHOUT_TIP:
    print("Рекомендуем оставить чаевые!")
else:
    print("Чаевые не требуются")
