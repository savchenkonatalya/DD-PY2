# TODO Написать 3 класса с документацией и аннотацией типов
class Student:
    """
    Документация на класс. Класс описывает оценки учащихся
    """
    def __init__(self, name: str, surname: str, grade: int):
        """
        Инициалзация экземпляра класса.
        :param name: имя
        :param surname: фамилия
        :param grade: оценка
        """
        self.name = name
        self.surname = surname
        if not isinstance(name and surname, str):
            raise TypeError("""Имя и фамилия должны быть списком """)
        self.grade = grade
        if 5 < grade < 0:
            raise ValueError("""Оценка должна принимать значение от 0 до 5 """)

    def change_grade(self, new_grade: int):
        ...
    """
    Метод изменяет оценку .
    :param new_grade: новая оценка .
    """
    def check_attestation(self) -> bool:
        ...
    """
    :return: аттестован ли студент.
    """


class Chair:
    """
    Документация на класс. Класс описывает одежду
    """
    def __init__(self, material: str, color: str):
        """
        Инициалзация экземпляра класса.
        :param material: материал одежды
        :color: цвет одежды
        """
        self.material = material
        self.color = color
        if not isinstance(material and color, str):
            raise TypeError("""Цвет и материал должны быть списком """)

    def check_price(self, price: int):
        ...
    """
    Цены одежды  с определенными атрибутами.
    :param price: стоимость одежды.
    """
    def change_color(self, new_color: str):
        ...
    """
    Метод изменяет цвет одежды.
    :param new_color: новый цвет стула.
    """


class Text:
    """
    Документация на класс. Класс описывает книгу
    """
    def __init__(self, pages: int, symbols: int):
        """
        Инициалзация экземпляра класса.
        :param pages: количество страниц в книге,
        :param symbols: количество символов в тексте
        """
        self.pages = pages
        self.symbols = symbols
        if not isinstance(pages and symbols, int):
            raise TypeError("""Количество страниц и символов в тексте - целое число """)
        if symbols and pages < 0:
            raise ValueError("""Количество страниц и символов не может быть отрицательным """)

    def increment_last_read_page(self, read_pages: int):
        ...
    """
    Метод увеличивает номер последней прочитанной страницы.
    :param read_pages: количество прочитанных страниц
    """
    def translate_text(self, language):
        ...
    """
    Метод переводит текст на другой язык.
    :param language: язык, на который необходимо перевести текст
    """


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
