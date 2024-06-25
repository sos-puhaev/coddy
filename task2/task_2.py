def total_hours(c1, b1):
    total_hours = 0
    while c1 > 0:
        # Каждый горит 2 часа
        total_hours += c1 * 2
        # Высчитываем новые огоньки
        new_fireworks = (c1 // b1) * 2
        # Обновляем кол-во огоньков
        c1 = new_fireworks
    return total_hours

# Известные данные
c1 = 10
b1 = 3
# Выводим общее кол-во часов.
print(total_hours(c1, b1))
