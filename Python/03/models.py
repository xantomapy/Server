__all__ = ['Person', 'Pupil', 'Employee']


class Person:
    def __init__(self):
        super().__init__()
        print('Constructor person')
        self.first_name = '-'
        self.last_name = '-'
        self.sex = '-'

    def __init__(self, first_name=None, last_name=None, sex=None):
        print('Constructor person')
        self._first_name = first_name
        self._last_name = last_name
        self._sex = sex

    def __del__(self):
        print('Destructor person')

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
        print('Constructor pupil')
        self.grade_class = 1
        self.specialization = '-'

    def __init__(self, first_name=None, last_name=None, sex=None, grade_class=None, specialization=None):
        super(Pupil, self).__init__(first_name, last_name, sex)
        print('Constructor pupil')
        self._grade_class = grade_class
        self._specialization = specialization

    def __del__(self):
        print('Destructor pupil')

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
        print('Constructor employee')
        self.position = '-'

    def __init__(self, first_name=None, last_name=None, sex=None, grade_class=None, specialization=None, position=None):
        super(Employee, self).__init__(first_name, last_name, sex, grade_class, specialization)
        print('Constructor employee')
        self._position = position

    def __del__(self):
        print('Destructor employee')

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

    def __str__(self):
        return (f'{self.full_name} position: {self.position} grade class: {self.grade_class} specialization: '
                f'{self.specialization}')
