stop_traffic_light_color = 'красный'
warning_traffic_light_color = 'желтый'
go_traffic_light_color = 'зеленый'

traffic_light_color = input(
    f'Введите цвет светофора ({stop_traffic_light_color}, {warning_traffic_light_color}, {go_traffic_light_color}): ')
traffic_light_color = traffic_light_color.strip().lower()
traffic_light_color = traffic_light_color.replace('ё', 'е')

if traffic_light_color == go_traffic_light_color:
    print('Едь')
else:
    if traffic_light_color == warning_traffic_light_color:
        print('Предупреждаю')
    else:
        if traffic_light_color == stop_traffic_light_color:
            print('Стоп')

print(f'Цвет введен неверно, он не соответствует ни одному из вариантов: {stop_traffic_light_color}, '
      f'{warning_traffic_light_color}, {go_traffic_light_color}')
