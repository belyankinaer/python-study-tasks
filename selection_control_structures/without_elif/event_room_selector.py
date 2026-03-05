participants_count = int(input("Введите количество участников мероприятия: "))

NO_PARTICIPANTS_COUNT = 0
SMALL_ROOM_PLACE_COUNT = 10
MEDIUM_ROOM_PLACE_COUNT = 50

if participants_count < NO_PARTICIPANTS_COUNT:
    print("Количество участников не может быть меньше либо равным нулю  ")
else:
    if participants_count <= SMALL_ROOM_PLACE_COUNT:
        print("Выбран малый зал")
    else:
        if participants_count <= MEDIUM_ROOM_PLACE_COUNT:
            print("Выбран средний зал")
        else:
            print("Выбран большой зал")
