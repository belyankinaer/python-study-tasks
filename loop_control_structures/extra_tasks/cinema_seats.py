MAX_CINEMA_SEATS = 120
SPLITTER = ' '

cinema_seats = ''

for seat_number in range(1, MAX_CINEMA_SEATS + 1):
    cinema_seats += f"{seat_number} "

user_seats_count_info = ''

while not user_seats_count_info.isdigit() or int(user_seats_count_info) < 0:
    user_seats_count_info = input(f"Введите количество мест для бронирования:")

user_seats_count = int(user_seats_count_info)

for seat in range(user_seats_count):
    is_seat_available = False
    user_seat_info = ''

    while not is_seat_available:
        while not user_seat_info.isdigit() or int(user_seat_info) < 0:
            user_seat_info = input(f"Введите желаемый номер места:")

        formated_user_seat_number = f"{user_seat_info}{SPLITTER}"

        if formated_user_seat_number in cinema_seats:
            cinema_seats = cinema_seats.replace(formated_user_seat_number, '')
            is_seat_available = True
            print(f"Место {user_seat_info} успешно забронировано!")
        else:
            is_seat_available = False
            print(f"Место {user_seat_info} занято, выберите другое.")
        user_seat_info = ''
