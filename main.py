class Student:
    """ Класс Студенты """
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        """ Добавление курса в завершенные """
        self.finished_courses.append(course_name)

    def rate_lesson(self, lecturer, course, grade):
        """ Выставление оценки за лекцию """
        if isinstance(lecturer, Lecturer) and 0 <= grade <= 10 and \
                course in self.courses_in_progress and \
                course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        """ Возвращает среднюю оценку """
        all_grades = []
        try:
            for grades in self.grades.values():
                all_grades += grades
            return sum(all_grades) / len(all_grades)
        except ZeroDivisionError:
            return 'Деление на 0. Ученик не проходит курсы в данный момент'

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка: {self._average_grade()}\n' \
               f'Курсы в процессе изучения: ' \
               f'{", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

    def __gt__(self, student):
        """ Возвращает self>value. """
        return self._average_grade() > student._average_grade()

    def __eq__(self, student):
        """ Возвращает self==value. """
        return self._average_grade() == student._average_grade()

    def __le__(self, student):
        """ Возвращает self<=value. """
        return self._average_grade() <= student._average_grade()


class Mentor:
    """ Класс Ментор """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """ Класс Лектор """
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        """ Возвращает среднюю оценку """
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка: {self._average_grade()}\n'

    def __gt__(self, lecturer):
        """ Возвращает self>value. """
        return self._average_grade() > lecturer._average_grade()

    def __eq__(self, lecturer):
        """ Возвращает self==value. """
        return self._average_grade() == lecturer._average_grade()

    def __le__(self, lecturer):
        """ Возвращает self<=value. """
        return self._average_grade() <= lecturer._average_grade()


class Reviewer(Mentor):
    """ Класс Эксперт """
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """ Выставление оценки за домашнюю работу """
        if isinstance(student, Student) and \
                course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname}\n'


def average_grade_students_course(students, course):
    """
    Подсчет средней оценки за домашние задания по всем студентам
    в рамках конкретного курса
    """
    all_grades = []
    for student in students:
        if course in student.grades.keys():
            all_grades += student.grades[course]
    return sum(all_grades) / len(all_grades)


def average_grade_lecturers_course(lecturers, course):
    """
    Подсчет средней оценки за лекции всех лекторов в рамках курса
    """
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades.keys():
            all_grades += lecturer.grades[course]
    return sum(all_grades) / len(all_grades)


