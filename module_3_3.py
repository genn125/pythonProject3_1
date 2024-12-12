
# module_3_3

# "Распаковка позиционных параметров" с выводом номера вызова ф-и

calls = 0
def count_calls():
    global calls
    calls += 1

def print_params(a = 1,  b = 'строка', c = True):
    count_calls()
    print(f'{calls:02d} -', a,b,c)     # :02d - Ноль перед 1-9

print_params(45, 90)             # 1.
print_params(45, 90, 180)     # 2. Вызовите функцию print_params с разным количеством аргументов,
print_params()                         # 3. включая вызов без аргументов
print_params(45)                       # 4.
print_params(45, b = 666, c = 180)  # 5.

print_params(b = 25)                   # 6. Проверьте, работают ли вызовы print_params(b = 25)
print_params(c = [1,2,3])              # 7. print_params(c = [1,2,3])

values_list = [1,'два', True]
values_dict = {'a' : 1.25,  'b' : 'строка', 'c' :None}
print_params(*values_list)             # 8. Передайте values_list
print_params(**values_dict)            # 9. и values_dict в функцию print_params, используя распаковку параметров

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2,42)     # 10. Проверьте, работает ли print_params(*values_list_2, 42)

def append_to_list(item, values_list=None):
    if values_list is None:
        values_list = []
        values_list.append(item)
print_params(*values_list)             # 11.
print_params(values_list)              # 12. Просто так)