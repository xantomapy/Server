from constants import PupilEnum
from models import Employee, Pupil, Person


def run():
    worker_1 = Employee(first_name='Max', last_name='Cros', sex='male', grade_class=11, specialization='IT',
                        position='programer')
    worker_2 = Employee(first_name='Alexandra', last_name='Chevdar', sex='female', grade_class=10, specialization='designer',
                        position='StreatArtCompany')
    worker_3 = Employee(first_name='Roman', last_name='Baskov', sex='male', grade_class=6, specialization='signer',
                        position='solist')
    worker_1.append(worker_2)
    worker_1.append(worker_3)
    worker_1.show_colleagues()

    employee = Employee(first_name='Roman', last_name='Baskov', sex='male', grade_class=6, specialization='signer',
                        position='solist')
    pupil = Pupil(first_name='Valentina', last_name='Nekrasova', sex='female', grade_class=8, specialization='Person')
    person = Person(first_name='Vova', last_name='Vist', sex='Male')

    print('*' * 8)

    worker_1.sort(PupilEnum.GRADE_CLASS.value)
    worker_1.show_colleagues()

    print('*' * 8)

    worker_1.pop()
    worker_1.show_colleagues()

    print('*' * 8)
    print(f'Size of: worker_1 is: {employee.__sizeof__()}')
    print(f'Size of: worker_2 is: {pupil.__sizeof__()}')
    print(f'Size of: worker_3 is: {person.__sizeof__()}')


if __name__ == '__main__':
    run()
