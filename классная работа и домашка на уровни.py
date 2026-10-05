def level1():
    text1 = "пРиВет МИР"
    print("Уровень 1: upper(), lower(), capitalize()")
    print("str.upper() - переводит все символы в верхний регистр")
    print("str.lower() - переводит все символы в нижний регистр")
    print("str.capitalize() - первая буква заглавная, остальные строчные")
    print("Примеры для строки 'пРиВет МИР':")
    print("  text.lower()      -> привет мир")
    print("  text.upper()      -> ПРИВЕТ МИР")
    print("  text.capitalize() -> Привет мир")
    print(f"Исходный текст для работы: '{text1}'")
 
    a = input("Выбрать метод (lower, upper, capitalize): ").strip().lower()
    a = a.replace("str.", "").replace("()", "")
 
    if a == "lower":
        return f"Результат: {text1.lower()}"
    if a == "upper":
        return f"Результат: {text1.upper()}"
    if a == "capitalize":
        return f"Результат: {text1.capitalize()}"
    return "Такого метода нет"
 
 
def level2():
    text2 = "Ботать это круто. Очень круто"
    print("Уровень 2: find(), replace(), count()")
    print("find() - индекс первого вхождения подстроки, -1, если не найдено")
    print("replace() - замена подстроки")
    print("count() - количество вхождений")
    print("Примеры для строки 'пРивет МИР':")
    print("  text.find('М') -> 7")
    print("  text.replace('МИР', 'все') -> пРивет все")
    print("  text.count('и') -> 1")
    print(f"Исходный текст для работы: '{text2}'")
 
    a = input("Выбрать метод (find, replace, count): ").strip().lower()
    a = a.replace("()", "")
 
    if a == "find":
        podstr = input("Ввести подстроку для поиска: ")
        return f"Результат (первое вхождение): {text2.find(podstr)}"
    if a == "replace":
        old = input("Что заменить? ")
        new = input("На что заменить? ")
        return f"Результат: {text2.replace(old, new)}"
    if a == "count":
        podstr = input("Какую подстроку посчитать? ")
        return f"Результат (кол-во вхождений): {text2.count(podstr)}"
    return "Такого метода нет"


def level3():
    text3 = "1,2,3,4"
    print("Уровень 3: split(), join()")
    print("split() - разбивает строку на список по разделителю")
    print("join() - собирает список обратно в строку через разделитель")
    print("Пример: '1,2,3,4'.split(',') -> ['1', '2', '3', '4']")
    print("Пример: '-'.join(['1', '2', '3', '4']) -> 1 2 3 4")
    print(f"Исходный текст для работы: '{text3}'")

    a = input ("Выбрать метод (split, join,): ").strip().lower()
    a = a.replace ("str.", "").replace("()", "")

    if a == "split":
        sep = input("Введите разделитель: ")
        if sep == "":
            return "Разделитель не может быть пустым"
        return f"Результат: {text3.split(sep)}"
    elif a == "join":
        sep = input("Чем соединить элементы? ")
        spisok = text3.split(",")
        return f"Результат: {sep.join(spisok)}"
    else:
        return "Нет такого метода"


def level4():
    text4a = "1234*&%$"
    text4b = "    abc1234    "
    print("Уровень 4: isdigit(), isalpha(), strip(), format()")
    print("isdigit() - True, если все символы цифры")
    print("isalpha() - True, если все символы буквы")
    print("strip() - убирает пробелы по краям lstrip - слева, rstrip - справа")
    print("format() - вставляет значение в {} шаблона")
    print(f"Текст 1: '{text4a}'")
    print(f"Текст 2: '{text4b}'")
 
    a = input("Выбрать метод (isdigit, isalpha, strip, format): ").strip().lower()
    a = a.replace("str.", "").replace("()", "")
 
    if a == "isdigit":
        return f"Текст 1: {text4a.isdigit()}, Текст 2: {text4b.isdigit()}"
    if a == "isalpha":
        return f"Текст 1: {text4a.isalpha()}, Текст 2: {text4b.isalpha()}"
    if a == "strip":
        vid = input("Какой вариант (strip, lstrip, rstrip)? ").strip().lower()
        if vid == "strip":
            return f"Результат: '{text4b.strip()}'"
        if vid == "lstrip":
            return f"Результат: '{text4b.lstrip()}'"
        if vid == "rstrip":
            return f"Результат: '{text4b.rstrip()}'"
        return "Такого варианта нет"
    if a == "format":
        shablon = "Привет, {}!"
        print(f"Шаблон: '{shablon}'")
        name = input("Введите имя: ")
        return shablon.format(name)
    return "Такого метода нет"
 
 
def level5():
    text5 = "     pYtHon is: AWESome...   "
    print("Уровень 5: приводим строку к красивой фразе")
    print(f"Исходная строка: '{text5}'")
 
    text5 = text5.strip()
    print(f"strip() убрал пробелы по краям: '{text5}'")
 
    text5 = text5.strip(".")
    print(f"strip('.') убраны точки по краям: '{text5}'")
 
    text5 = text5.replace(":", "")
    print(f"replace(':', '') убрал двоеточие: '{text5}'")
 
    text5 = text5.capitalize()
    print(f"capitalize() первая буква заглавная, остальные строчные: '{text5}'")
 
    slova = text5.split()
    text5 = " ".join(slova)
    print(f"split() и join() убрали лишние пробелы: '{text5}'")
 
    return f"Результат: {text5}"
 
 
g = input("Выберите уровень 1 - 5: ")
if g == "1":
    print(level1())
elif g == "2":
    print(level2())
elif g == "3":
    print(level3())
elif g == "4":
    print(level4())
elif g == "5":
    print(level5())
else:
    print("Такого уровня нет")
