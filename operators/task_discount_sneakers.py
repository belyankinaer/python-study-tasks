sneakers_price = int(input('Введите сумму покупки: '))
max_without_discount_sneakers_price = 5000

if sneakers_price > max_without_discount_sneakers_price:
    sneakers_price = sneakers_price * 0.95

print(f'Сумма к оплате: {sneakers_price}')
