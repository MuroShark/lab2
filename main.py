for Р in range(1, 10):  # Р не может быть 0
    for А in range(0, 10):
        for Д in range(0, 10):
            # Проверяем, что все цифры различны
            if len({Р, А, Д}) == 3:
                # Вычисляем значение выражения (Р + А + Д)^4
                left_side = (Р + А + Д) ** 4
                # Формируем число РАДАР, используя цифры
                right_side = int(f"{Р}{А}{Д}{А}{Р}")
                # Сравниваем результаты
                if left_side == right_side:
                    print(f"Р = {Р}, А = {А}, Д = {Д}")
# Добавление изменения с локального репозитория Visual Studio
