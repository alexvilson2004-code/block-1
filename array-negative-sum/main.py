"""Сумма отрицательных элементов между максимумом и минимумом массива."""


def sum_negative_between_extremes(array: list[int]) -> int:
    """Находит сумму отрицательных элементов между max и min.

    Если max или min встречается несколько раз, используется первое вхождение.
    Сами максимальный и минимальный элементы в сумму не входят.
    """
    if not array:
        raise ValueError("Массив не должен быть пустым.")

    # Находим индексы первых вхождений максимального и минимального элементов.
    max_index = array.index(max(array))
    min_index = array.index(min(array))

    # Границы задаём по возрастанию, чтобы обработать оба порядка элементов.
    left = min(max_index, min_index)
    right = max(max_index, min_index)

    # Берём элементы строго между максимумом и минимумом
    # и складываем только отрицательные.
    return sum(value for value in array[left + 1:right] if value < 0)


def main() -> None:
    """Считывает массив, выводит его и результат вычислений."""
    try:
        n = int(input("Введите размер массива N: "))
        if n <= 0:
            print("Размер массива должен быть положительным.")
            return

        values = input(f"Введите {n} целых чисел через пробел: ").split()

        if len(values) != n:
            print(f"Ошибка: нужно ввести ровно {n} чисел.")
            return

        array = [int(value) for value in values]
        result = sum_negative_between_extremes(array)

        print(f"Массив A: {array}")
        print(f"Сумма отрицательных элементов между max и min: {result}")

    except ValueError:
        print("Ошибка ввода: введите целые числа.")


if __name__ == "__main__":
    main()
