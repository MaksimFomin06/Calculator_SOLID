"""Модуль отвечающий за работу с меню"""

import abc


class BaseCalculatorMenu(abc.ABC):
    """Абстрактный класс, описывающий интерфейс работы с меню"""

    _start_menu_text: tuple[str, ...]
    _choice_number_type_text: str
    _enter_one_int_number_text: str
    _enter_one_float_number_text: str
    _answer_text: str
    _history_text: str
    _error_answer: str

    @classmethod
    @abc.abstractmethod
    def set_start_menu_items(cls, menu_items: list[str]) -> None:
        """
        Установка пунктов меню выбора

        :param menu_items: Список с элементами меню
        :type menu_items: list[str]
        """

    @classmethod
    @abc.abstractmethod
    def get_start_menu(cls) -> tuple[str, ...]:
        """
        Получение стартового меню выбора

        :return: Меню в виде кортежа с текстом
        :rtype: tuple[str, ...]
        """

    @classmethod
    @abc.abstractmethod
    def get_choice_number_type_text(cls) -> str:
        """
        Получение текста для информирования о необходимости ввести тип числа

        :return: Фраза в виде текста
        :rtype: str
        """

    @classmethod
    @abc.abstractmethod
    def get_enter_one_int_number_text(cls) -> str:
        """
        Получение текста для информирования о необходимости ввести одно целое число

        :return: Фраза в виде текста
        :rtype: str
        """

    @classmethod
    @abc.abstractmethod
    def get_enter_one_float_number_text(cls) -> str:
        """
        Получение текста для информирования о необходимости ввести одно вещественное число

        :return: Фраза в вие текста
        :rtype: str
        """

    @classmethod
    @abc.abstractmethod
    def get_answer_text(cls) -> str:
        """
        Получение текста для информирования о том, что сейчас будет выведен ответ

        :return: Фраза в виде текста
        :rtype: str
        """

    @classmethod
    @abc.abstractmethod
    def get_history_text(cls) -> str:
        """
        Получение текста для информирования о том, что сейчас будет выведена история

        :return: _description_
        :rtype: str
        """
    
    @classmethod
    @abc.abstractmethod
    def answer_error(cls) -> str:
        """
        Получение текста для информации о том, что сработала ошибка ввода

        :return: Фраза в виде текста
        :rtype: str
        """


class CalculatorMenu(BaseCalculatorMenu):

    _start_menu_text = tuple()
    _choice_number_type_text = "Введите тип числа (int или float"
    _enter_one_int_number_text = "Введите одно целое число"
    _enter_one_float_number_text = "Введите одно вещественное число"
    _answer_text = "Ответ:"
    _history_text = "История операций:"
    _error_answer = "Ошибка ввода"

    @classmethod
    def set_start_menu_items(cls, menu_items: list[str]) -> None:
        
        cls._start_menu_text = (
            "Выберите пункт меню:",
            *(f"{index + 1}. {menu_items[index]}" for index in range(len(menu_items))),
        )

    @classmethod
    def get_start_menu(cls) -> tuple[str, ...]:
        return cls._start_menu_text

    @classmethod
    def get_choice_number_type_text(cls) -> str:
        return cls._choice_number_type_text

    @classmethod
    def get_enter_one_int_number_text(cls) -> str:
        return cls._enter_one_int_number_text

    @classmethod
    def get_enter_one_float_number_text(cls) -> str:
        return cls._enter_one_float_number_text

    @classmethod
    def get_answer_text(cls) -> str:
        return cls._answer_text

    @classmethod
    def get_history_text(cls) -> str:
        return cls._history_text
    
    @classmethod
    def answer_error(cls) -> str:
        return cls._error_answer
