from typing import TYPE_CHECKING

__all__ = ['connect']


if TYPE_CHECKING:
    from app.mainwindow import MainWindow


def connect(cls: 'MainWindow'):
    connection_screen(cls)
    control_employee_screen(cls)


def connection_screen(cls: 'MainWindow'):
    cls.window.connect_btn.clicked.connect(cls.connect_click)


def control_employee_screen(cls: 'MainWindow'):
    cls.window.add_employee_btn.clicked.connect(cls.add_employee_btn_click)
    cls.window.show_employees_btn.clicked.connect(cls.show_employees_btn_click)
    cls.window.delete_employees_btn.clicked.connect(cls.delete_employees_btn_click)
