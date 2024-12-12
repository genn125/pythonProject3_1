
# Module_3_5

# Рекурсия - замена .replace(старый, новый, сколько)

def get_multiplied_digits(number):

    str_number = str(number)

    if len(str_number) > 1:

        str_number = str_number.replace('0', '1')       # Заменить 0 на 1

        first = int(str_number[0])                                  # Взять первый символ

        return first * get_multiplied_digits(int(str_number[1:]))   # Умножить первую цифру числа на результат работы
                                                                    # этой же функции с числом, но уже без первой цифры

    else:
        return int(str_number)


print(get_multiplied_digits(402030000))
print(get_multiplied_digits(402030))

print(get_multiplied_digits(4524))