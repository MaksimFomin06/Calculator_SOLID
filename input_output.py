"""Модуль, отвечающий за операции ввода/вывода"""

import abc


class BaseInput(abc.ABC):
    """Абстрактный класс, описывающий интерфейс работы с вводом данных"""

    @staticmethod
    @abc.abstractmethod
    def get_one_int_number() -> int:
        """
        Получение одного целого числа

        :return: Одно целое число
        :rtype: int
        """

    @staticmethod
    @abc.abstractmethod
    def get_one_float_number() -> float:
        """
        Получение одного вещественного числа

        :return: Одно вещественное число
        :rtype: float
        """

    @staticmethod
    @abc.abstractmethod
    def get_text() -> str:
        """
        Получение строчки текста

        :return: Текстовая строка
        :rtype: str
        """


class BaseOutput(abc.ABC):
    """Абстрактный класс, опивающий интерфейс работы с выводом данных"""

    @staticmethod
    @abc.abstractmethod
    def output_one_line_text(text: str) -> None:
        """
        Вывод текста

        :param text: Текст, который нужно вывести
        :type text: str
        """

    @staticmethod
    @abc.abstractmethod
    def output_text_lines(text_lines: tuple[str, ...]) -> None:
        """
        Вывод строк текста

        :param text_lines: Кортеж со строками текста
        :type text_lines: tuple[str, ...]
        """


class BaseInputOutput(BaseInput, BaseOutput):
    """Абстрактный класс, который объединять интерфейсы ввода и вывода"""


class ConsoleInputOutput(BaseInputOutput):
    """Реализация ввода и вывода через консоль"""

    @staticmethod
    def get_one_int_number() -> int:
        return int(input())

    @staticmethod
    def get_one_float_number() -> float:
        return float(input())

    @staticmethod
    def get_text() -> str:
        return input()

    @staticmethod
    def output_one_line_text(text: str) -> None:
        print(text)

    @staticmethod
    def output_text_lines(text_lines: tuple[str, ...]) -> None:
        print(*text_lines, sep="\n")
