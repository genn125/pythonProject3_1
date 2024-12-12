
# module_3_1.py

# "Пространство имён" --- Подсчёт вызовов функции

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()  # Считать кол элементов строки,-
                                                        # - перевод в верхний и нижний регистры.
def is_contains (string, list_to_search):
    count_calls()

    # return string.upper() in [i.upper() for i in list_to_search]

    if string.upper() in [i.upper() for i in list_to_search]:    # Проверить, есть ли элемент в списке,-
                                                                 # -приведя все элементы к верхнему регистру.

        print(True, f"строка <{string}> находится в списке <{', '.join(list_to_search)}>", sep=", ", end=".\n")
    else:
        print(False, f"строкИ <{string}> нет в списке <{', '.join(list_to_search)}>", sep=", ", end=".\n\n")

print(string_info('Capybara'), end=".\n")
print(string_info('Armageddon'), end=".\n\n")

is_contains('ban', ['ban', 'BaNaNб', 'urBAN'])
is_contains('cycle', ['recycle', 'cyclic'])

print('Количество вызовов функции -', calls)