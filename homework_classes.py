# 1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_info(self):
        return f"{self.name}, {self.age} years."


Vasya = Person("Иванов Василий Викторович", 11)

print(Vasya.get_info())
print(Vasya.get_name())
print(Vasya.get_age())


# 2

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_info(self):
        return f"{self.name}, {self.age} years."


class Student(Person):
    def __init__(self, name, age, grade, subjects):
        super().__init__(name, age)
        self.__grade = grade
        self.subjects = subjects

    def get_grade(self):
        return self.__grade

    def finish_grade(self):
        self.__grade += 1
        return self.__grade

    def get_info(self):
        subjects_str = "\n".join(self.subjects)
        return (f"{self.name}, {self.age} years.\n{self.__grade} "
                f"grade\nSubjects studying:\n{subjects_str}")


Vasya = Student("Иванов Василий Викторович", 11, 3, ["maths", "physics"])

print(Vasya.get_info())
print(Vasya.finish_grade())
print(Vasya.get_grade())
print(Vasya.get_age())


# 3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_info(self):
        return f"{self.name}, {self.age} years."


class Worker:
    def __init__(self, position, wage):
        self.position = position
        self.wage = wage

    def get_position(self):
        return self.position

    def get_wage(self):
        return self.wage


class Teacher(Person, Worker):
    def __init__(self, name, age, position, wage):
        super().__init__(name, age)
        self.position = position
        self.wage = wage

    def get_info(self):
        return (f"{self.name}, {self.age} years."
                f"{self.position}, wage: {self.wage} rub.")


Valera = Teacher("Ярцев Валерий Рустэмович", 20, "Informatics teacher", 200)

print(Valera.get_info())
print(Valera.get_wage())
print(Valera.get_age())


# 4

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_info(self):
        return f"{self.name}, {self.age} years."


class Student(Person):
    def __init__(self, name, age, grade, subjects):
        super().__init__(name, age)
        self.__grade = grade
        self.subjects = subjects

    def get_grade(self):
        return self.__grade

    def finish_grade(self):
        self.__grade += 1
        return self.__grade

    def get_info(self):
        subjects_str = "\n".join(self.subjects)
        return (f"{self.name}, {self.age} years."
                f"\n{self.__grade} grade"
                f"\nSubjects studying:\n{subjects_str}")


class Worker:
    def __init__(self, position, wage):
        self.position = position
        self.wage = wage

    def get_position(self):
        return self.position

    def get_wage(self):
        return self.wage


class Teacher(Person, Worker):
    def __init__(self, name, age, position, wage):
        super().__init__(name, age)
        self.position = position
        self.wage = wage

    def get_info(self):
        return (f"{self.name}, {self.age} years."
                f"{self.position}, wage: {self.wage} rub.")


class Group:
    def __init__(self, group_name, students, group_teacher):
        self.group_name = group_name
        self.students = students
        self.group_teacher = group_teacher

    def get_info(self):
        info = (f"Group {self.group_name}\nGroup teacher:"
                f"\n{self.group_teacher.get_info()}\nStudents:\n")
        student_infos = [student.get_info() for student in self.students]
        info += "\n".join(student_infos)
        return info

    def get_students_number(self):
        return len(self.students)


# Пример использования
student1 = Student("Виталий", 23, 3, ["Maths", "Physics"])
student2 = Student("Геннадий", 21, 3, ["Maths", "Physics"])
student3 = Student("Иван", 43, 3, ["Maths", "Physics", "PE"])
teacher = Teacher("Ярцев Валерий Рустэмович", 20, "Informatics teacher", 200)
group = Group("3A", [student1, student2, student3], teacher)

print(group.get_info())
print(group.get_students_number())

# 4

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, age, size, habitat):
        self.age = age
        self.size = size
        self.habitat = habitat

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"


class Cat(Animal):
    def make_sound(self):
        return "Мяу-мяу!"


class Dolphin(Animal):
    def make_sound(self):
        return "Клик-клик!"


class Elephant(Animal):
    def make_sound(self):
        return "Тру-у-у!"


class CircusAnimalEnsemble:
    def __init__(self, animals):
        self.animals = animals

    def speak(self):
        for animal in self.animals:
            print(animal.make_sound())


if __name__ == "__main__":
    dog = Dog(5, "средний", "дом")
    cat = Cat(3, "маленький", "квартира")
    dolphin = Dolphin(10, "крупный", "океан")
    elephant = Elephant(25, "огромный", "саванна")

    ensemble = CircusAnimalEnsemble([dog, cat, dolphin, elephant])
    ensemble.speak()
