
# module_3_2.py

# "Раз, два, три, четыре, пять .... Это не всё?":

def calculate_structure_sum (data_structure):
    summa = 0
    if isinstance(data_structure, dict):
        for i, j in data_structure.items():
            summa += calculate_structure_sum(i)
            summa += calculate_structure_sum(j)

    elif isinstance(data_structure, (int, float)):
        summa += data_structure

    elif isinstance(data_structure, str):
        summa += len(data_structure)

    elif isinstance(data_structure, (list, tuple, set)):
        for d in data_structure:
            summa += calculate_structure_sum(d)

    return summa

data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),
                  "Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

print(calculate_structure_sum(data_structure))