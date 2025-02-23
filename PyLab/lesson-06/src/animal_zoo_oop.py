from abc import ABC, abstractmethod
import uuid
import time


# Abstract Base Class (ABC) - a template/contract that defines common behavior
class Animal(ABC):
    """
    Abstract base class for all animals.

    OOP Concept #1: Encapsulation
    - We bundle related data (name, sex, id) and methods (cry) together in a class
    - We can control access to data using private/protected attributes
    """

    count = 0  # Class Property

    def __init__(self, name: str, sex: int):
        """
        Initialize an animal with basic properties.

        OOP Concept #2: Constructor
        - Special method that runs when creating a new object
        - Sets up the initial state of the object
        """
        self._name = name  # protected attribute (single underscore)
        self._sex = sex
        self._id = None  # will be set by child classes

        # Animal.count = Animal.count + 1
        self.accumulate_animal_count()

    @property
    def sex_str(self) -> str:
        """
        Property decorator - allows us to access method like an attribute.
        This is part of encapsulation - providing controlled access to data.
        """
        return "male" if self._sex == 0 else "female"

    @abstractmethod
    def cry(self):
        """
        Abstract method - must be implemented by all child classes.

        OOP Concept #3: Abstraction
        - Hide complex implementation details
        - Force child classes to implement certain methods
        """
        pass

    @staticmethod
    def generate_unique_id(prefix: str = "") -> str:
        """Generate a unique ID."""
        timestamp = (int(time.time() * 1000) >> 3) % 11451
        unique_string = str(uuid.uuid4().hex[:6])
        return f"{prefix}{timestamp}_{unique_string}"

    @classmethod
    def accumulate_animal_count(cls, count: int = 1):
        cls.count += count


class Cat(Animal):
    """
    Cat class inheriting from Animal.

    OOP Concept #4: Inheritance
    - Cat is-a Animal
    - Inherits all Animal attributes and methods
    - Can override methods to provide specific behavior
    """

    def __init__(self, name: str, sex: int, color: str):
        """
        Initialize a cat with specific properties.

        OOP Concept #5: Super
        - Call parent class's methods using super()
        - Ensures proper initialization of parent class
        """
        super().__init__(name, sex)
        self._color = color
        self._id = self.generate_unique_id("cat")

    def cry(self):
        """
        OOP Concept #6: Polymorphism
        - Same method name (cry) but different behavior for each animal
        - Allows us to treat different objects uniformly
        """
        print(
            f"Hi, I am Cat. My name is {self._name}. "
            f"I am a {self.sex_str} cat. "
            f"My ID is {self._id}. "
            f"My color is {self._color}."
        )


class Dog(Animal):
    def __init__(self, name: str, sex: int, weight: int):
        super().__init__(name, sex)
        self._weight = weight
        self._id = Animal.generate_unique_id("dog")
        self.count = 100

    def cry(self):
        print(
            f"Hi, I am Dog. My name is {self._name}. "
            f"I am a {self.sex_str} dog. "
            f"My ID is {self._id}. "
            f"My weight is {self._weight}kg."
        )


class Duck(Animal):
    def __init__(self, name: str, sex: int, age: int):
        super().__init__(name, sex)
        self._age = age
        self._id = Cat.generate_unique_id("duck")

    def cry(self):
        print(
            f"Hi, I am Duck. My name is {self._name}. "
            f"I am a {self.sex_str} duck. "
            f"My ID is {self._id}. "
            f"I am {self._age} years old."
        )


def main():
    """
    OOP Advantages Demonstrated:
    1. Code Organization: Related data and behavior are bundled together
    2. Reusability: Animal class can be reused for any new animal
    3. Maintainability: Changes to base behavior can be made in one place
    4. Flexibility: New animals can be added without changing existing code
    5. Modularity: Each class is independent and can be modified separately
    """

    # Create a list of different animals
    animals = [Cat("Kitty", 0, "red"), Dog("Peter", 1, 20), Duck("Donald", 0, 3)]

    # Demonstrate polymorphism - same method call, different behavior
    for animal in animals:
        animal.cry()

    print(f"There are {Animal.count} animals in total.")


if __name__ == "__main__":
    main()
