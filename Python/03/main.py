from models import Employee


def run():
    worker_1 = Employee(first_name='Vlad', last_name='Petrov', sex='male', grade_class=11, specialization='Customer',
                        position='Archmeister')
    worker_2 = Employee()
    worker_2.first_name = 'Vlada'
    worker_2.last_name = 'Petrova'
    worker_2.sex = 'female'
    worker_2.grade_class = 7
    worker_2.specialization = 'Manager'
    worker_2.position = 'Butik'

    worker_3 = Employee()
    worker_3.read()

    print(worker_1)
    print(worker_2)
    print(worker_3)


if __name__ == '__main__':
    run()
