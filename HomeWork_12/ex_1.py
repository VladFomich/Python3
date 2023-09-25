# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре 
# недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам 
# всех предметов вместе взятых.

import csv


class NameValidator:

    def __get__(self, instance, owner):

        return instance.__dict__[self.name]

    

    def __set__(self, instance, value):

        if not value[0].isupper() or not value.isalpha():

            raise ValueError('Не верный формат имени')

        instance.__dict__[self.name] = value

    

    def __set_name__(self, owner, name):

        self.name = name



class SubjectValidator:

    def __get__(self, instance, owner):

        return instance.__dict__[self.name]

    

    def __set__(self, instance, value):

        with open('../subjects.csv') as file:

            subjects = [subject[0] for subject in csv.reader(file)]

        if value not in subjects:

            raise ValueError('Не верный предмет')

        instance.__dict__[self.name] = value

    

    def __set_name__(self, owner, name):

        self.name = name



class ScoreValidator:

    def __get__(self, instance, owner):

        return instance.__dict__[self.name]

    

    def __set__(self, instance, value):

        try:

            value = float(value)

            if value < 0 or value > 100:

                raise ValueError()

        except:

            raise ValueError('Не верные баллы')

        instance.__dict__[self.name] = value

    

    def __set_name__(self, owner, name):

        self.name = name



class MarkValidator:

    def __get__(self, instance, owner):

        return instance.__dict__[self.name]

    

    def __set__(self, instance, value):

        try:

            value = int(value)

            if value < 2 or value > 5:

                raise ValueError()

        except:

            raise ValueError('Не верная оценка')

        instance.__dict__[self.name] = value

    

    def __set_name__(self, owner, name):

        self.name = name



class Student:

    name = NameValidator()

    subject = SubjectValidator()

    score = ScoreValidator()

    mark = MarkValidator()

    

    def __init__(self, name, subjects):

        self.name = name

        self.subjects = subjects

    

    def __str__(self):

        return f"Студент: {self.name}"

    

    def add_subject_result(self, subject, score=None, mark=None):

        if subject not in self.subjects:

            raise ValueError('Не верный предмет')

        if score is not None and mark is not None:

            raise ValueError('Баллы и оценка не найдены')

        if score is None and mark is None:

            raise ValueError('Баллы и оценки не найдены')

        if score is not None:

            if subject not in self.__dict__:

                self.__dict__[subject] = { 'баллы': [], 'оценки': [] }

            self.__dict__[subject]['баллы'].append(score)

        else:

            if subject not in self.__dict__:

                self.__dict__[subject] = { 'баллы': [], 'оценки': [] }

            self.__dict__[subject]['оценки'].append(mark)

    

    def get_subject_average_score(self, subject):

        try:

            scores = self.__dict__[subject]['баллы']

            return sum(scores) / len(scores)

        except:

            raise ValueError('Не верный предмет')

    

    def get_total_average_score(self):

        total_scores = []

        for subject in self.subjects:

            try:

                scores = self.__dict__[subject]['баллы']

                total_scores += scores

            except:

                pass

        return sum(total_scores) / len(total_scores)



subjects = ['Математика', 'Физика', 'Химия']

student = Student('Иван Иванов', subjects)

print(student)

student.add_subject_result('Математика', score=90)

student.add_subject_result('Математика', score=80)

student.add_subject_result('Математика', score=100)

print(student.get_subject_average_score('Математика'))

student.add_subject_result('Физика', mark=5)

student.add_subject_result('Физика', mark=4)

student.add_subject_result('Физика', mark=3)

print(student.get_subject_average_score('Физика'))

print(student.get_total_average_score())