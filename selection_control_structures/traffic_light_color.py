STOP_TRAFFIC_LIGHT_COLOR = 'красный'
WARNING_TRAFFIC_LIGHT_COLOR = 'желтый'
GO_TRAFFIC_LIGHT_COLOR = 'зеленый'

traffic_light_color = input(
    f'Введите цвет светофора ({STOP_TRAFFIC_LIGHT_COLOR}, {WARNING_TRAFFIC_LIGHT_COLOR}, {GO_TRAFFIC_LIGHT_COLOR}): ')
traffic_light_color = traffic_light_color.strip().lower()

SYMBOL_FOR_REPLACE = 'ё'
SYMBOL_FOR_REPLACE_TO = 'е'
traffic_light_color = traffic_light_color.replace(SYMBOL_FOR_REPLACE, SYMBOL_FOR_REPLACE_TO)

if traffic_light_color == GO_TRAFFIC_LIGHT_COLOR:
    print('Едь')
elif traffic_light_color == WARNING_TRAFFIC_LIGHT_COLOR:
    print('Предупреждаю')
elif traffic_light_color == STOP_TRAFFIC_LIGHT_COLOR:
    print('Стоп')
else:
    print(f'Цвет введен неверно, он не соответствует ни одному из вариантов: {STOP_TRAFFIC_LIGHT_COLOR}, '
          f'{WARNING_TRAFFIC_LIGHT_COLOR}, {GO_TRAFFIC_LIGHT_COLOR}')
