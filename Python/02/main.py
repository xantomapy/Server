class Employee:
    """ Class describe typically employee """
    counter = 0

    def __init__(self):
        Employee.counter += 1
        print(Employee.counter)

    def __init__(self, name='John', position='Analytic'):
        Employee.counter += 1
        print(Employee.counter)
        try:
            self.__name = name
            self.__position = position
        except ValueError:
            print(ValueError)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def your_position(self):
        return print(f'My position is: {self.position}')

    def your_name(self):
        return print(f'My name is: {self.name}')


if __name__ == '__main__':
    human_1 = Employee()

    human_1.name = 'Billy'
    human_1.position = 'Switcher'

    human_1.your_name()
    human_1.your_position()

    print(('=' * 5) + 'Human 2' + ('=' * 5))

    human_2 = Employee('Max', 'Translator')

    human_2.your_name()
    human_2.your_position()
