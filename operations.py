"""Модуль, отвечающий за математические операции"""

import abc


class BaseOperation(abc.ABC):
    """Абстрактный класс, описывающий интерфейс работы с математической операцией"""

    @staticmethod
    @abc.abstractmethod
    def calculate(number_one: int | float, number_two: int | float) -> int | float:
        """
        Вычисление математической операции

        :param number_one: Первое число
        :type number_one: int | float
        :param number_two: Второе число
        :type number_two: int | float
        :return: Результат вычисления
        :rtype: int | float
        """

    @staticmethod
    @abc.abstractmethod
    def get_calculate_str(number_one: int | float, number_two: int | float) -> str:
        """
        Вычисление математической операции и получение результата в виде строки

        :param number_one: Первое число
        :type number_one: int | float
        :param number_two: Второе число
        :type number_two: int | float
        :return: Результат вычисление в виде строки
        :rtype: str
        """


class OperationSumma(BaseOperation):
    """Реализация поиска суммы"""

    @staticmethod
    def calculate(number_one: int | float, number_two: int | float) -> int | float:
        return number_one + number_two

    @staticmethod
    def get_calculate_str(number_one: int | float, number_two: int | float) -> str:
        return f"{number_one} + {number_two} = {OperationSumma.calculate(number_one, number_two)}"


class OperationDifferences(BaseOperation):
    """Реализация поиска разности"""

    @staticmethod
    def calculate(number_one: int | float, number_two: int | float) -> int | float:
        return number_one - number_two

    @staticmethod
    def get_calculate_str(number_one: int | float, number_two: int | float) -> str:
        return f"{number_one} - {number_two} = {OperationDifferences.calculate(number_one, number_two)}"


class OperationMultiplication(BaseOperation):
    """Реализация умножения"""

    @staticmethod
    def calculate(number_one: int | float, number_two: int | float) -> int | float:
        return number_one * number_two

    @staticmethod
    def get_calculate_str(number_one: int | float, number_two: int | float) -> str:
        return f"{number_one} * {number_two} = {OperationMultiplication.calculate(number_one, number_two)}"


class OperationDivisions(BaseOperation):
    """Реализация деления"""

    @staticmethod
    def calculate(number_one: int | float, number_two: int | float) -> int | float:
        return number_one / number_two

    @staticmethod
    def get_calculate_str(number_one: int | float, number_two: int | float) -> str:
        return f"{number_one} / {number_two} = {OperationDivisions.calculate(number_one, number_two)}"


class OperationPercentage(BaseOperation):
    """Реализация поиска процента от числа"""

    @staticmethod
    def calculate(number_one: int | float, number_two: int | float) -> int | float:
        return number_one / 100 * number_two

    @staticmethod
    def get_calculate_str(number_one: int | float, number_two: int | float) -> str:
        return f"{number_one} / 100 * {number_two} = {OperationPercentage.calculate(number_one, number_two)}"

