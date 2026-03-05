previous_purchase_amount = int(input("Введите сумму предыдущих покупок: "))
current_purchase_amount = int(input("Введите сумму текущей покупки: "))

NO_DISCOUNT_MIN_AMOUNT = 1000
FIVE_PERCENT_MAX_AMOUNT = 5000
FULL_PERCENT = 100

if previous_purchase_amount < NO_DISCOUNT_MIN_AMOUNT:
    print("Скидка не предоставляется")
    print(f"Итоговая сумма: {current_purchase_amount}")
else:

    if previous_purchase_amount <= FIVE_PERCENT_MAX_AMOUNT:
        discount_percent = 5
    else:
        discount_percent = 10

    discount_price = (current_purchase_amount * discount_percent) / FULL_PERCENT
    current_purchase_amount = current_purchase_amount - discount_price

    print(f"Скидка: {discount_percent}%")
    print(f"Итоговая сумма: {current_purchase_amount}")
