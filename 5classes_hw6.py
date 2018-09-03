# Создайте класс Student, который содержит атрибуты: фамилия и инициалы, номер группы, успеваемость
# (массив из пяти элементов). Создать массив(студентов) из десяти элементов такого типа, упорядочить записи по
#  возрастанию среднего балла.
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.

class Student:
    def __init__(self, rank, fullname=None, group_num=0):
        self._students = []
        self.fullname = fullname
        self.group_num = group_num
        self.rank = rank

    def print_info(self):
        print('_______________________________________________________________________________________________________')
        print('Name: ', self.fullname)
        print('Group number: ', self.group_num)
        print('Rank: ', self.rank)
        print('Average rank: ', self.average_rank())
        print('______________________________________________________________________________________________________')

    def average_rank(self):
        self.average_rank = sum(self.rank)/5
        return self.average_rank

    def add_student(self, student):
        if student not in self._students:
            self._students.append(student)

    def remove_student(self, student):
        if student in self._students:
            self._students.remove(student)

    @staticmethod
    def filter_students(list_of_students):
        res = sorted(list_of_students, key=lambda st: st.average_rank(), reverse=True)
            # this block only for check and print result.
        for elem in res:
            print(elem.fullname, '=', elem.average_rank)
        return res
    @staticmethod
    def print_high_rank(list_of_students):
        print('___________________________________________________________________')
        print('Students that have average rank more than 4:')
        for st in list_of_students:
            if st.average_rank >= 4:
                print(st.fullname, '=', st.average_rank, ', group number:', st.group_num)


st1 = Student([5, 4, 2, 3, 1], 'Dao Anna', 5)
st2 = Student([5, 4, 2, 3, 4], 'Stadnichenko Valeriy', 4)
st3 = Student([3, 0, 2, 1, 5], 'Lazebniy Timur', 2)
st4 = Student([4, 4, 4, 4, 5], 'Verdi Olga', 3)
st5 = Student([5, 4, 5, 0, 4], 'Kovalchuk Dasha', 1)
st6 = Student([5, 4, 2, 2, 3], 'Reshetnik Vlad', 1)
st7 = Student([2, 4, 2, 4, 2], 'Untilov Serezha', 3)
st8 = Student([4, 4, 5, 5, 5], 'Martinuyk Katya', 5)
st9 = Student([4, 4, 2, 3, 2], 'Stavertii Anastasia', 2)
st10 = Student([2, 4, 2, 2, 4], 'Severinenko Lera', 3)

list_of_students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]
Student.filter_students(list_of_students)
Student.print_high_rank(list_of_students)






