from abc import ABC, abstractmethod


class Ward:
    def __init__(self, name):
        self._name = name
        self._list_of_person = []

    def add_person(self, person):
        self._list_of_person.append(person)

    def describe(self):
        print(f'Ward name: {self._name}')
        for person in self._list_of_person:
            person.describe()

    def count_doctor(self):
        n_doctors = 0
        for person in self._list_of_person:
            if type(person) == Doctor:
                n_doctors += 1
        return n_doctors

    def sort_age(self):
        self._list_of_person.sort(key=lambda person: person._yob, reverse=True)

    def compute_average(self):
        teacher_yob = [
            person._yob for person in self._list_of_person if type(person) == Teacher]
        return round(sum(teacher_yob)/len(teacher_yob), 0)


class Person(ABC):
    @abstractmethod
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(
            f'Student - Name: {self._name} - Yob: {self._yob} - Grade: {self._grade}')


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f'Student - Name: {self._name} - Yob: {self._yob} - Subject: {self._subject}')


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f'Student - Name: {self._name} - Yob: {self._yob} - Specialist: {self._specialist}')


student1 = Student(name=" studentA ", yob=2010, grade="7")
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")

ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

print(f"\nNumber of doctors : {ward1.count_doctor()}")

print("\nAfter sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()

print(f"\nAverage year of birth ( teachers ): {ward1.compute_average()}")
