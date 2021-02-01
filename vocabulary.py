voc = {'explicit': "явный", 'implicit': "не явный", 'complex': "сложный", 'complicated': "усложнённый",
       'flat': "плоский", 'nested': "вложенный", 'share': "делиться", 'vowels': "гласные", 'breadth': "широта", 'width': "ширина", 'immutable': "неизменный",
       'editor': "редактор", 'vanish': "исчезать", 'even': "чётный", 'pappy': "бодрый", 'draw': "ничья", 'lesion': "поражение", 'amount of': "количество",
       'scope': "область видимости", 'growth': "рост", 'general': "общее", 'mean': "среднее", 'array': "массив",
       'breed': "порода", 'overloading': "перегрузка", 'regex': "регулярное выражение"
       }
new_voc = {'query': "запрос", 'hence': "следовательно", 'employ': "употреблять", 'insufficiently': "недостаточно",
           'consume': "поглощать", 'parse': "анализ", 'raw': "сырой", 'concatenate': "соединять", 'gaps': "пробелы", 'instance': "пример", 'execution': "выполнение",
           'suspend': "приостанавливать", 'rearrange': "перестраивать", 'tough': "жёсткий", 'entire': "весь", 'peril': "риск", 'property': "свойство",
           'shallow': "мелкий", 'data': "данные", 'multiplier': "множитель", 'solitude': "одиночество", 'capacity': "вместимость", 'resolution': "разрешение",
           'inheritance': "наследство", 'inappropriate': "неуместный", 'appropriate': "соответствующий", 'apply': "применять", 'overall': "в общем",
           'define': "определять", 'perform': "выполнять", 'performance': "эффективность", 'substitute': "замена", 'quality': "качество",  'expression': "выражение",
           'impression': "впечатление", 'assembly': "сборка", 'sophisticate': "не простой", 'issue': "спорный вопрос", 'dash': "тире", 'delimiter': "разделитель", 'loop': "петля",
           'row': "ряд", 'quotes': "кавычки", 'likewise': "точно так же", 'quantity': "величина", 'addition': "дополнение", 'indent': "отступ", 'require': "требовать",
           'twilight': "сумерки", 'dusk': "сумрак", 'established': "установлен", 'swap': "обмен", 'sever': "отрезать", 'sewer': "коллектор", 'resign': "уход в отставку", 'obtain': "получить",
           'item': "пункт"}

work = 'on'
while work != 'off':
    print()
    word = 'in'
    work = input("""
    1. Перевод нового слова --- 11. Перевод старого слова
    2. Show new words in english --- 21. Sorted alphabetically
    3. Показать новые слова на русском --- 31. Сортировка по алфавиту
    4. Показать весь старый словарь --- 41. Показать весь новый словарь
    5. Show old words in english --- 51. Sorted alphabetically
    6. Показать старые слова на русском --- 61. Сортировка по алфавиту
    7. Завершить работу
    
Enter the appropriate number: """)
    if work not in ('1','11', '2', '21', '3', '31', '4', '41', '5', '51', '6', '61', '7'):
        print('Wrong number. Try again.')
    elif work == '2':
        number = 0
        print()
        work = "1"
        for key, value in new_voc.items():
            number += 1
            if number % 15 == 0:
                print()
            print(key, end=' - ')
        print()
    elif work == '21':
        number = 0
        print()
        work = "1"
        abc_words = sorted(new_voc.keys())
        for key in abc_words:
            number += 1
            if number % 15 == 0:
                print()
            print(key, end=' - ')
        print()
    elif work == '3':
        number = 0
        print()
        work = "1"
        for key, value in new_voc.items():
            number += 1
            if number % 15 == 0:
                print()
            print(value, end=' - ')
        print()
    elif work == '31':
        number = 0
        print()
        work = "1"
        abc_words = sorted(new_voc.values())
        for value in abc_words:
            number += 1
            if number % 15 == 0:
                print()
            print(value, end=' - ')
        print()
    elif work == '4':
        number = 0
        print()
        work = "1"
        for key, value in voc.items():
            number += 1
            if number % 8 == 0:
                print()
            print(key, value, sep='-', end=' , ')
        print()
    elif work == '41':
        number = 0
        print()
        work = "1"
        for key, value in new_voc.items():
            number += 1
            if number % 8 == 0:
                print()
            print(key, value, sep='-', end=' , ')
        print()
    elif work == '5':
        number = 0
        print()
        work = "11"
        for key, value in voc.items():
            number += 1
            if number % 15 == 0:
                print()
            print(key, end=' - ')
        print()
    elif work == '51':
        number = 0
        print()
        work = "11"
        abc_words = sorted(voc.keys())
        for key in abc_words:
            number += 1
            if number % 15 == 0:
                print()
            print(key, end=' - ')
        print()
    elif work == '6':
        number = 0
        print()
        work = "11"
        for key, value in voc.items():
            number += 1
            if number % 15 == 0:
                print()
            print(value, end=' - ')
        print()
    elif work == '61':
        number = 0
        print()
        work = "11"
        abc_words = sorted(voc.values())
        for value in abc_words:
            number += 1
            if number % 15 == 0:
                print()
            print(value, end=' - ')
        print()
    if work == '1':
        while word != 'out':
            word = input("Input 1 to exit or word for translate: ").lower()
            if word in new_voc.keys():
                print(f'Translation of the:  - - - - - - - - - {word} -', new_voc[word])
            elif word in new_voc.values():
                for key, value in new_voc.items():
                    if value == word:
                        print(f'Перевод слова: - - - - - - - - - - - - {word} -', key)
            elif word == '1':
                word = 'out'
                break
            else:
                print('There is no such word in the dictionary. Try again.')
    elif work == '11':
        while word != 'out':
            word = input("Input 1 to exit or word for translate: ").lower()
            if word in voc.keys():
                print(f'Translation of the:  - - - - - - - - - {word} -', voc[word])
            elif word in voc.values():
                for key, value in voc.items():
                    if value == word:
                        print(f'Перевод слова: - - - - - - - - - - - - {word} -', key)
            elif word == '1':
                word = 'out'
                break
            else:
                print('There is no such word in the dictionary. Try again.')
    elif work == '7':
        print('bye bye')
        work = 'off'
