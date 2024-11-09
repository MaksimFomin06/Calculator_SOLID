"""Модуль, отвечающий за работу проекта (сборка всех частей вместе)"""

import abc
import copy

import history
import input_output
import menu
import operations


class BaseCalculatorMain(abc.ABC):
    """Абстрактный класс, описывающий интерфейс взаимодействия с проектом 'Калькулятор'"""

    @abc.abstractmethod
    def __init__(
        self,
        input_output_object: input_output.BaseInputOutput,
        history_object: history.BaseHistory,
        menu_object: menu.BaseCalculatorMenu,
        operations_list: list[operations.BaseOperation],
    ) -> None:
        self._input_output_object: input_output.BaseInputOutput
        self._history_object: history.BaseHistory
        self._menu_object: menu.BaseCalculatorMenu
        self._operations_list: list[operations.BaseOperation]

    @abc.abstractmethod
    def change_components(
        self,
        input_output_object: input_output.BaseInputOutput | None,
        history_object: history.BaseHistory | None,
        menu_object: menu.BaseCalculatorMenu | None,
        operations_list: list[operations.BaseOperation] | None,
    ) -> None:
        """
        Изменение компонентов калькулятора при необходимости

        :param input_output_object: Объект, отвечающий за ввод/вывод данных, может быть None, если замена не требуется
        :type input_output_object: input_output.BaseInputOutput | None
        :param history_object: Объект, отвечающий за работу с историей, может быть None, если замена не требуется
        :type history_object: history.BaseHistory | None
        :param menu_object: Объект, отвечающий за работу с меню, может быть None, если замена не требуется
        :type menu_object: menu.BaseCalculatorMenu | None
        :param operations_list: Список с операциями, может быть None, если замена не требуется
        :type operations_list: list[operations.BaseOperation] | None
        """

    @abc.abstractmethod
    def run(self) -> None:
        """Запуск работы калькулятора"""


class CalculatorMain(BaseCalculatorMain):
    """Реализация работы калькулятора"""

    def __init__(
        self,
        input_output_object: input_output.BaseInputOutput,
        history_object: history.BaseHistory,
        menu_object: menu.BaseCalculatorMenu,
        operations_list: list[operations.BaseOperation],
    ) -> None:
        self._input_output_object = input_output_object
        self._history_object = history_object
        self._menu_object = menu_object
        self._operations_list = copy.copy(operations_list)

    def change_components(
        self,
        input_output_object: input_output.BaseInputOutput | None,
        history_object: history.BaseHistory | None,
        menu_object: menu.BaseCalculatorMenu | None,
        operations_list: list[operations.BaseOperation] | None,
    ) -> None:
        if not input_output_object is None:
            self._input_output_object = input_output_object
        if not history_object is None:
            self._history_object = history_object
        if not menu_object is None:
            self._menu_object = menu_object
        if not operations_list is None:
            self._operations_list = copy.copy(operations_list)

    def run(self) -> None:
        while True:
            self._input_output_object.output_text_lines(self._menu_object.get_start_menu())
            self._input_output_object.output_one_line_text(self._menu_object.get_enter_one_int_number_text())
            user_operation_choice: int = self._input_output_object.get_one_int_number()
            self._input_output_object.output_one_line_text(self._menu_object.get_choice_number_type_text())
            user_first_number: int | float = 0
            user_second_number: int | float = 0
            user_type_choice: str = self._input_output_object.get_text()
            if user_type_choice == "int":
                self._input_output_object.output_one_line_text(self._menu_object.get_enter_one_int_number_text())
                user_first_number = self._input_output_object.get_one_int_number()
            elif user_type_choice == "float":
                self._input_output_object.output_one_line_text(self._menu_object.get_enter_one_float_number_text())
                user_first_number = self._input_output_object.get_one_float_number()
            self._input_output_object.output_one_line_text(self._menu_object.get_choice_number_type_text())
            user_type_choice = self._input_output_object.get_text()
            if user_type_choice == "int":
                self._input_output_object.output_one_line_text(self._menu_object.get_enter_one_int_number_text())
                user_second_number = self._input_output_object.get_one_int_number()
            elif user_type_choice == "float":
                self._input_output_object.output_one_line_text(self._menu_object.get_enter_one_float_number_text())
                user_second_number = self._input_output_object.get_one_float_number()
            answer: int | float = self._operations_list[user_operation_choice - 1].calculate(
                user_first_number, user_second_number
            )
            self._input_output_object.output_one_line_text(self._menu_object.get_answer_text())
            self._input_output_object.output_one_line_text(str(answer))
            self._history_object.add_operation(
                self._operations_list[user_operation_choice - 1].get_calculate_str(
                    user_first_number, user_second_number
                )
            )
            self._input_output_object.output_one_line_text(self._menu_object.get_history_text())
            self._input_output_object.output_text_lines(self._history_object.get_history())


def main() -> None:
    """main-функция"""

    operation_name_list: list[str] = ["Сложение", "Вычитание", "Умножение", "Деление", "Нахождение процента"]
    menu_object: menu.CalculatorMenu = menu.CalculatorMenu()
    menu_object.set_start_menu_items(operation_name_list)
    operation_list: list[operations.BaseOperation] = [
        operations.OperationSumma(),
        operations.OperationDifferences(),
        operations.OperationMultiplication(),
        operations.OperationDivisions(),
        operations.OperationPercentage(),
    ]
    calculator: CalculatorMain = CalculatorMain(
        input_output.ConsoleInputOutput(), history.History(), menu_object, operation_list
    )
    calculator.run()


if __name__ == "__main__":
    main()
