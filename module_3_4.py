
# module_3_4.py

# "Однокоренные" - использования параметров *args/ **kwargs на практике

def single_root_words(*other_words, root_words='гриб'):
    same_words = []

    for i in other_words:

        if root_words.lower() in i.lower() or i.lower() in root_words.lower():
            same_words.append(i)

    return print(same_words)

single_root_words('грибник', 'гриБной', 'гробница', 'грибОЧЕк')
single_root_words('Чёрный', 'Обе', 'двЕ', 'ЛИС',
                  root_words = 'обелиск')

