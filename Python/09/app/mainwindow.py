# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QTableWidgetItem
from PySide2 import QtWidgets, QtUiTools

from app.action_connector import connect
from app.config import MAIN_WINDOW_UI, DB, DB_USERNAME, DB_PASSWORD
from app.constants import PupilEnum
from app.models import Employee, WorkerController, DBConnector


class MainWindow:
    def __init__(self):
        self.maintainer = WorkerController()
        self.db_connector = DBConnector()

    def init_gui(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.loader = QtUiTools.QUiLoader()
        self.window = self.loader.load(MAIN_WINDOW_UI, None)
        self.connect_actions()

    def connect_actions(self):
        """ Using for connect class functionality to buttons """
        connect(self)

    def parse_fields(self) -> dict:
        """ Получает данные из строк ввода """
        return {
            PupilEnum.POSITION.value: self.window.creation_position_edit.text(),
            PupilEnum.SPECIALIZATION.value: self.window.creation_specialization_edit.text(),
            PupilEnum.GRADE_CLASS.value: self.window.creation_grade_class_edit.text(),
            PupilEnum.SEX.value: self.window.creation_sex_edit.text(),
            PupilEnum.LAST_NAME.value: self.window.creation_second_name_edit.text(),
            PupilEnum.FIRST_NAME.value: self.window.creation_first_name_edit.text(),
        }

    def add_employee_btn_click(self):
        """ Добавляет сотрудника в список сотрудников """
        parsed = self.parse_fields()
        employee = Employee(
            position=parsed[PupilEnum.POSITION.value],
            specialization=parsed[PupilEnum.SPECIALIZATION.value],
            grade_class=parsed[PupilEnum.GRADE_CLASS.value],
            sex=parsed[PupilEnum.SEX.value],
            last_name=parsed[PupilEnum.LAST_NAME.value],
            first_name=parsed[PupilEnum.FIRST_NAME.value],
        )
        self.db_connector.insert_data(employee)

    def connect_click(self) -> None:
        db = self.window.connection_db_name_edit.text()
        db_username = self.window.eonnection_username_edit.text()
        db_password = self.window.connection_password_edit.text()

        self.db_connector.connect(DB, DB_USERNAME, DB_PASSWORD)
        # self.db_connector.connect(db, db_username, db_password)
        self.switch_to_screen(page=1)

    def switch_to_screen(self, page: int = 1) -> None:
        self.window.stackedWidget.setCurrentIndex(page)

    def show_employees_btn_click(self):
        self.set_table_data(self.db_connector.show_data())

    def set_table_data(self, data):
        data = list(data)
        self.window.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.window.tableWidget.setItem(i, j, QTableWidgetItem(data[i][j]))

    def delete_employees_btn_click(self):
        self.db_connector.remove_data(self.window.creation_id_edit.text())


def init_gui():
    window = MainWindow()
    window.init_gui()

    window.window.show()
    sys.exit(window.app.exec_())
