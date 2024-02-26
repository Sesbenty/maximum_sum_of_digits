def max_sum_digits() -> int:
    value, max_value = int(input()), 0
    while value != 0:
        new_max = sum_digits(value)
        if new_max > max_value:
            max_value = new_max
        value = int(input())
    return max_value


def sum_digits(value: int) -> int:
    current = value if value > 0 else -value
    digit, result = current % 10, 0
    while current != 0:
        result += digit
        current = int(current / 10)
        digit = current % 10
    return result


def main_menu():
    print('maximum_sum_of_digits v1 by Alexander Shanin')
    print('\nВвод чисел:')
    result = max_sum_digits()
    print(f'Максимальная сумма чиссел: {result}')
    input('...')


if __name__ == '__main__':
    main_menu()
