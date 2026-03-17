from random import randint

MAX_CINEMA_SEATS = 120
SPLITTER = ' '

cinema_seats = []

for seat_number in range(1, MAX_CINEMA_SEATS + 1):
    is_seat_free = bool(randint(0, 1))
    print(f"МестоЖ: {seat_number}, свободно: {is_seat_free}")
    cinema_seats.append(is_seat_free)

user_seats_count_info = ''

while not user_seats_count_info.isdigit() or int(user_seats_count_info) < 0:
    user_seats_count_info = input(f"Введите количество мест для бронирования:")
user_seats_count = int(user_seats_count_info)

user_seats_numbers = []
for seat in range(user_seats_count):
    is_seat_available = False
    user_seat_info = ''

    while not is_seat_available:
        while not user_seat_info.isdigit() or int(user_seat_info) < 0:
            user_seat_info = input(f"Введите желаемый номер места:")
            user_seat_number = int(user_seat_info)

        is_seat_free = cinema_seats[user_seat_number - 1]

        if is_seat_free:
            cinema_seats[user_seat_number - 1] = False
            user_seats_numbers.append(user_seat_number)
            print(f"Место {user_seat_info} успешно забронировано!")
            is_seat_available = True
        else:
            print(f"Место {user_seat_info} занято, выберите другое.")
        user_seat_info = ''

user_seats_numbers_info = ''
user_seats_numbers.sort()

for user_seat_number in user_seats_numbers:
    user_seats_numbers_info += str(user_seat_number) + SPLITTER
print(f"Вы забронировали места: {user_seats_numbers_info}")
