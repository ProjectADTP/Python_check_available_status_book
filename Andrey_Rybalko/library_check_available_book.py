YES = "yes"
NO = "no"

def book_list_view(current_library):
    if not current_library:
        print("Библиотека пуста!")
    else:
        print("В библиотеке имеются следующие книги: " + ", ".join(book for book in current_library.keys()))


def add_book(book_name, author, year, library):
    if not validate_book_data(book_name, author, year):
        return

    if book_name in library:
        if not can_update_info(book_name):
            print("Изменение отменено!")
            return
        else:
            current_availability = library[book_name].get("available")
            library[book_name] = {"author": author, "year": year, "available": current_availability}
            print("Информация о книге обновлена!")
            return

    library[book_name] = {"author": author, "year": year, "available": None}
    print(f"Книга \"{book_name}\" успешно добавлена в библиотеку!")


def try_change_available_status(book_name, library):
    while True:
        answer = input(f"Статус наличия книги \"{book_name}\" не определён!\n"
              "Желаете его изменить? (yes/no): ")
        if answer == YES:
            set_available_status(book_name, library)
            return True
        elif answer == NO:
            return False
        else:
            print("Введите корректный ответ (yes/no)")


def set_available_status(book_name, library):
    while True:
        answer = input(f"Какой статус наличия книги установить? (yes/no): ")
        if answer == YES:
            library[book_name]["available"] = True
            return
        elif answer == NO:
            library[book_name]["available"] = False
            return
        else:
            print("Введите корректный ответ(yes/no)")


def _update_book_availability(book_name, library, available):
    if not check_book_in_library(book_name, library):
        return False

    if library[book_name]["available"] is None and not try_change_available_status(book_name, library):
        return False

    if library[book_name]["available"] == available:
        action = "в библиотеке" if available else "выдана"
        print(f"Книга \"{book_name}\" уже {action}!")
        return False

    library[book_name]["available"] = available
    action = "возвращена" if available else "выдана"

    print(f"Книга \"{book_name}\" {action}!")
    return True


def issue_book(book_name, library):
    _update_book_availability(book_name, library, False)


def return_book(book_name, library):
    _update_book_availability(book_name, library, True)


def check_book_in_library(book_name, library):
    if book_name in library:
        return True
    print(f"\nКниги \"{book_name}\" нет в библиотеке!")
    return False


def find_book(book_name, library):
    if not check_book_in_library(book_name, library):
        return

    print(
        f"\nНаименование книги: \"{book_name}\"\n"
        f"Автор: {library[book_name]['author']}\n"
        f"Год издания: {library[book_name]['year']}"
    )

    print_book_available_status(book_name, library)


def print_book_available_status(book_name, library):
    status = library[book_name]['available']
    if status:
        print(f"Книга доступна")
    elif status is None:
        print(f"Книга в библиотеке, но ее статус не определен")
    else:
        print(f"Книга выдана")


def remove_book(book_name, library):
    if check_book_in_library(book_name, library):
        del library[book_name]

        print(f"Книга \"{book_name}\" успешно удалена из библиотеки!")


def can_update_info(book_name):
    while True:
        answer = input(
            f"Книга \"{book_name}\" уже имеется в библиотеке!\n"
            "Желаете обновить информацию о ней? (yes/no): "
        ).lower()
        if answer == YES:
            return True
        elif answer == NO:
            return False
        else:
            print("Введите корректный ответ(yes/no)")


def validate_book_data(book_name, author, year):
    if not isinstance(book_name, str) or not book_name.strip():
        print("Ошибка! Название должно быть строкой!")
        return False

    if not isinstance(author, str) or not author.strip():
        print("Ошибка! Автор должен быть строкой!")
        return False

    if not isinstance(year, int) or year < 0:
        print("Ошибка! Год должен быть положительным числом!")
        return False

    return True


def get_library():
    library = {
        "Преступление и наказание": {
            "author": "Фёдор Достоевский",
            "year": 1866,
            "available": True,
        },
        "Война и мир": {
            "author": "Лев Толстой",
            "year": 1869,
            "available": True,
        },
        "Мастер и Маргарита": {
            "author": "Михаил Булгаков",
            "year": 1967,
            "available": False,
        },
        "1984": {
            "author": "Джордж Оруэлл",
            "year": 1949,
            "available": True,
        },
        "Гарри Поттер и философский камень": {
            "author": "Дж. К. Роулинг",
            "year": 1997,
            "available": True,
        },
        "Властелин колец": {
            "author": "Дж. Р. Р. Толкин",
            "year": 1954,
            "available": True,
        },
    }

    return library


def program():
    library = get_library()
    book_list_view(library)

    add_book("Гарри Поттер и философский камень", "Дж. К. Роулинг", 1111, library)
    book_list_view(library)

    add_book("Гарри Поттер и Тайная комната", "Дж. К. Роулинг", 1998, library)
    book_list_view(library)

    remove_book("Абоба", library)
    remove_book("Преступление и наказание", library)
    book_list_view(library)

    issue_book("Aboba", library)
    return_book("Aboba", library)
    issue_book("Гарри Поттер и Тайная комната", library)
    return_book("Гарри Поттер и Тайная комната", library)
    issue_book("Властелин колец", library)
    issue_book("Властелин колец", library)
    return_book("Властелин колец", library)
    return_book("Властелин колец", library)

    find_book("Мастер и Маргарита", library)
    find_book("C# Для Начинающих на практике", library)
    find_book("1984", library)
    find_book("Гарри Поттер и Тайная комната", library)

program()