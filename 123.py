def binary(number): # Перевод из десятичного кода в двоичный
    if number == 0:
        return '0'
    result = ''
    while number:
        result += str(number % 2)
        number //= 2
    return result[::-1]
print(binary(6))
