"""Модуль, отвечающий за работу с историей"""

import abc


class BaseHistory(abc.ABC):
    """Абстрактный класс, описывающий интерфейс работы с историей вычислений"""

    @abc.abstractmethod
    def __init__(self) -> None:
        self._history_list: list[str]

    @abc.abstractmethod
    def add_operation(self, operation: str) -> None:
        """
        Добавление операции в историю

        :param operation: Операция в виде строки
        :type operation: str
        """

    @abc.abstractmethod
    def get_history(self) -> tuple[str, ...]:
        """
        Получение операций в виде кортежа строк

        :return: Кортеж с операциями
        :rtype: tuple[str, ...]
        """


class History(BaseHistory):
    """Реализация работы с историей"""

    def __init__(self) -> None:
        self._history_list = []

    def add_operation(self, operation: str) -> None:
        self._history_list.append(operation)

    def get_history(self) -> tuple[str, ...]:
        return tuple(self._history_list)
