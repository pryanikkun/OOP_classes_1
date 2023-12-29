from main import Student, Mentor, Reviewer, Lecturer, \
    average_grade_lecturers_course, average_grade_students_course


# Экземпляры класса Студент
first_student = Student('Sonya', 'Ivanova', 'female')
first_student.courses_in_progress += ['Python', 'Django']
first_student.finished_courses += ['Git']

second_student = Student('Sasha', 'Ivanov', 'male')
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Введение в анализ данных']

third_student = Student('Sonya', 'Ivanova', 'female')  # для последней проверки
third_student.courses_in_progress += ['Python', 'Django']
third_student.finished_courses += ['Git']

# Экземпляры класса Ментор

mentor_1 = Mentor('Olga', 'Revina')
mentor_1.courses_attached += ['Python', 'Git']

mentor_2 = Mentor('Sergey', 'Revin')
mentor_2.courses_attached += ['Django']

# Экземпляры класса Лектор

lecturer_1 = Lecturer('Emma', 'Rodinova')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Egor', 'Imashev')
lecturer_2.courses_attached += ['Django']

lecturer_3 = Lecturer('Emma', 'Rodinova')  # для последней проверки
lecturer_3.courses_attached += ['Python', 'Git']

# Экземпляры класса Эксперт

reviewer_1 = Reviewer('Ivan', 'Sokolov')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Igor', 'Suvorov')
reviewer_2.courses_attached += ['Git', 'Django']

# Выставление оценки за дз экспертом
reviewer_1.rate_hw(first_student, 'Python', 10)
reviewer_2.rate_hw(first_student, 'Python', 10)
reviewer_1.rate_hw(first_student, 'Python', 7)
print(first_student.grades)

reviewer_1.rate_hw(second_student, 'Git', 10)
reviewer_2.rate_hw(second_student, 'Python', 10)
reviewer_2.rate_hw(second_student, 'Git', 7)
print(second_student.grades)

reviewer_1.rate_hw(third_student, 'Python', 10)
reviewer_1.rate_hw(third_student, 'Python', 7)
print(third_student.grades)

# Выставление оценки лектору за лекцию
first_student.rate_lesson(lecturer_1, 'Python', 6)  # зачлось
first_student.rate_lesson(lecturer_2, 'Django', 10)  # да
first_student.rate_lesson(lecturer_1, 'Python', 7)  # да

second_student.rate_lesson(lecturer_1, 'Git', 10)  # да
second_student.rate_lesson(lecturer_2, 'Python', 10)  # нет
second_student.rate_lesson(lecturer_1, 'Git', 7)  # да

second_student.rate_lesson(lecturer_3, 'Git', 4)
second_student.rate_lesson(lecturer_3, 'Git', 7)

print(lecturer_1.grades)
print(lecturer_2.grades)

# Метод __str__
print(first_student)
print(lecturer_1)
print(reviewer_1)

# Сравнение объектов класса Студент
print(first_student > second_student)  # 8.5 > 7
print(first_student == second_student)
print(first_student >= second_student)

# Сравнение объектов класса Лектор
print(lecturer_1 < lecturer_2)  # 7.5 > 10
print(lecturer_1 != lecturer_2)
print(lecturer_1 <= lecturer_2)

# Проверим функции подсчета среднего по всем студентам
students = [first_student, second_student, third_student]
print(average_grade_students_course(students, 'Python'))

lecturers = [lecturer_1, lecturer_2, lecturer_3]
print(average_grade_lecturers_course(lecturers, 'Git'))
