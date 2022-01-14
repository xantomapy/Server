__all__ = ['Person', 'Pupil', 'Employee', 'WorkerController', 'DBConnector']

from mysql import connector
from mysql.connector import connect, Error

from app.config import DB, DB_HOST


class Person:
    def __init__(self):
        super().__init__()
        self.first_name = '-'
        self.last_name = '-'
        self.sex = '-'

    def __init__(self, first_name=None, last_name=None, sex=None):
        self._first_name = first_name
        self._last_name = last_name
        self._sex = sex

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, sex):
        self._sex = sex

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Pupil(Person):
    def __init__(self):
        super().__init__()
        self.grade_class = 1
        self.specialization = '-'

    def __init__(self, first_name=None, last_name=None, sex=None, grade_class=None, specialization=None):
        super(Pupil, self).__init__(first_name, last_name, sex)
        self._grade_class = grade_class
        self._specialization = specialization

    @property
    def grade_class(self):
        return self._grade_class

    @grade_class.setter
    def grade_class(self, grade_class: int):
        self._grade_class = int(grade_class)

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, specialization):
        self._specialization = specialization

    def __str__(self):
        return f'{self.full_name} {self.sex} grade class: {self.grade_class} specialization: {self.specialization}'


class Employee(Pupil):
    def __init__(self):
        super().__init__()
        self.position = '-'
        self.colleagues = []

    def __init__(self, first_name=None, last_name=None, sex=None, grade_class=None, specialization=None, position=None):
        super(Employee, self).__init__(first_name, last_name, sex, grade_class, specialization)
        self._position = position
        self.colleagues = []

    def __str__(self):
        return (f'{self.full_name}, sex: {self.sex}, position: {self.position} grade class: {self.grade_class}'
                f' specialization: {self.specialization}')

    def __getitem__(self, key):
        return getattr(self, key)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    def read(self):
        print('Enter first name below:')
        self.first_name = input()

        print('Enter last name below:')
        self.last_name = input()

        print('Enter sex below:')
        self.sex = input()

        print('Enter pupil grade_class below:')
        self.grade_class = int(input())

        print('Enter pupil specialization below:')
        self.specialization = input()

        print('Enter position in library for pupil below:')
        self.position = input()

    def append(self, item: Pupil) -> None:
        self.colleagues.append(item)

    def pop(self) -> Pupil:
        self.colleagues.pop()

    def show_colleagues(self) -> None:
        return print('\n'.join(''.join(str(col)) for col in self.colleagues))

    def sort(self, key):
        return self.colleagues.sort(key=lambda x: x[key])


class WorkerController:
    def __init__(self):
        self.workers = []

    def show_workers(self):
        print('******** workers ********')
        if not self.workers:
            print('No one worker in container')
        for worker in self.workers:
            print(worker)

    def sort(self, key):
        if not self.workers:
            print('No one worker for sorting')
        else:
            print(f'Sorted by: {key}')
        return self.workers.sort(key=lambda x: x[key])

    def append(self, item: Employee) -> None:
        self.workers.append(item)

    def pop(self):
        self.workers.pop()


class DBConnector:

    connect = connector

    def __init__(self):
        self.db_host = DB_HOST

    def connect(self, db: str = '', username: str = '', db_password: str = ''):
        try:
            self.connect = connector.connect(
                database=db,
                host=self.db_host,
                user=username,
                password=db_password
            )
            with connect(
            ) as connection:
                print(connection)
        except Error as e:
            print(e)

    def insert_data(self, e: Employee) -> None:
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(f"""
                    INSERT INTO employee (grade_class, sex, last_name, specialization, position, first_name)
                    VALUES
                        ("{e.grade_class}", "{e.sex}", "{e.last_name}", "{e.specialization}", "{e.position}", "{e.first_name}")
                """)
                self.connect.commit()
        except Error as e:
            print(e)

    def show_data(self) -> tuple:
        try:
            result = ()
            with self.connect.cursor() as cursor:
                cursor.execute("""SELECT * FROM employee;""")
                result = cursor.fetchall()
                for row in result:
                    print(row)
        except Error as e:
            print(e)

        return result

    def remove_data(self, e_id: int) -> None:
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(f"""DELETE FROM employee WHERE id={e_id}""")
                self.connect.commit()
        except Error as e:
            print(e)
