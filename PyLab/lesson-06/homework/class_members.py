from abc import ABC, abstractmethod
import uuid
import time
import random


class Person:
    """
    Requirements
    ------------
        `Person` should be an abstract base class which CANNOT be instantiated.

        `Person` class should contain the following CLASS variables:
        1. population
        2. average_age

        `Person` class should contain the following methods:
        1. generate_uid(), static, generate a unique ID.
        2. generate_name(), static, generate a random english name.
        3. generate_age(), static, generate a random age between (0, 100).
        2. say_hello(), abstract API, say name, id, gender, age and other infos.

        `Person` instance should contain the following INSTANCE variables:
        1. name
        2. id
        3. gender
        4. age

    """

    population = 0
    sum_ages = 0

    @staticmethod
    def generate_uid(prefix: str = "") -> str:
        timestamp = (int(time.time() * 1000) >> 3) % 11451
        unique_string = str(uuid.uuid4().hex[:6])
        return f"{prefix}{timestamp}_{unique_string}"

    @classmethod
    def average_age(cls):
        if cls.population == 0:
            return 0
        return cls.sum_ages / cls.population

    @staticmethod
    def generate_age():
        return random.randint(0, 100)

    @staticmethod
    def generate_name():
        names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank"]
        return random.choice(names)

    @abstractmethod
    def say_hello(self):
        pass

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.uid = self.generate_uid("Person")
        Person.population += 1
        Person.sum_ages += age


class Student(Person):
    """
    Requirements
    ------------
        `Student` should be a derived class from `Person`, which CAN be instantiated.

        Besides thoes members inhereted from the base class:

        A `Student` instance should contain the following INSTANCE variables:
        1. hobby

        A `Student` class should contain the following method:
        1. generate_random_hobby(), static, pick a random hobby from
            ['basketball', 'soccer', 'tennis', 'ballet', 'tango', 'piano', 'guitar']
    """

    @staticmethod
    def generate_hobby():
        hobbies = [
            "basketball",
            "soccer",
            "tennis",
            "ballet",
            "tango",
            "piano",
            "guitar",
        ]
        return random.choice(hobbies)

    def __init__(self, name, age, gender, hobby):
        super().__init__(name, age, gender)
        self.hobby = hobby
        self.uid = Person.generate_uid("Student")

    def say_hello(self):
        print(
            f"Hello! My name is {self.name}, UID: {self.uid},"
            f"Gender: {self.gender}, Age: {self.age}, Hobby: {self.hobby}."
        )


class Teacher(Person):
    """
    Requirements
    ------------
        `Teacher` should be a derived class from `Person`, which CAN be instantiated.

        Besides thoes members inhereted from the base class:

        A `Student` instance should contain the following INSTANCE variables:
        1. favorate_cartoon_charactor

        A `Teacher` class should contain the following method:
        1. generate_random_cartoon_charactor(), static, pick a random name from:
            ['Yukino Yukinoshita', 'Shinobu Oshino', 'Mashiro Shiina', 'Makise Kurisu']
    """

    @staticmethod
    def generate_random_cartoon_charactor():
        cartoon_charactors = [
            "Yukino Yukinoshita",
            "Shinobu Oshino",
            "Mashiro Shiina",
            "Makise Kurisu",
        ]
        return random.choice(cartoon_charactors)

    def __init__(self, name, age, gender, favorate_cartoon_charactor):
        super().__init__(name, age, gender)
        self.favorate_cartoon_charactor = favorate_cartoon_charactor
        self.uid = Person.generate_uid("Teacher")

    def say_hello(self):
        print(
            f"Hello! My name is {self.name}, UID: {self.uid},"
            f"Gender: {self.gender}, Age: {self.age}, "
            f"Favorate cartoon charactor: {self.favorate_cartoon_charactor}."
        )


def main():
    # 1. Instantiate `Person`, catch the exception, and warn users they should not instantiate
    #    an ABC.

    try:
        person = Person("Bob", "1", "Male", 30, "reading")
    except TypeError:
        print("TypeError")

    # 2. Create a list of persons, append 10 Teachers or Students randomly.
    persons: list[Person] = []
    for _ in range(10):
        if random.choice([True, False]):
            name = Person.generate_name()
            age = Person.generate_age()
            gender = random.choice(["Male", "Female"])
            hobby = Student.generate_hobby()
            persons.append(Student(name, age, gender, hobby))
        else:
            name = Person.generate_name()
            age = Person.generate_age()
            gender = random.choice(["Male", "Female"])
            favorate_cartoon_charactor = Teacher.generate_random_cartoon_charactor()
            persons.append(Teacher(name, age, gender, favorate_cartoon_charactor))

    # 3. For every person in the list, invoke funtion `say_hello()`.
    for person in persons:
        person.say_hello()

    print(f"Population: {Person.population}")
    print(f"Average Age: {Person.average_age()}")


if __name__ == "__main__":
    main()
