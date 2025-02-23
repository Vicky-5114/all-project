import uuid
import time


def generate_unique_id(prefix: str = "") -> str:
    """
    Generate a unique ID.

    Parameters
    ----------
    prefix : str, optional
        Optinal prefix, by default ""

    Returns
    -------
    str
        A unique ID, for example: "1492_c0d230".
    """
    timestamp = (int(time.time() * 1000) >> 3) % 11451
    unique_string = str(uuid.uuid4().hex[:6])
    return f"{prefix}{timestamp}_{unique_string}"


sex_i2s = lambda sex: "male" if sex == 0 else "female"

animal_count = 0


def create_cat(name: str, sex: int, color: str):
    global animal_count
    animal_count = animal_count + 1
    return name, sex, generate_unique_id("cat"), color


def create_dog(name: str, sex: int, weight: int):
    global animal_count
    animal_count = animal_count + 1
    return name, sex, generate_unique_id("dog"), weight


def create_duck(name: str, sex: int, age: int):
    global animal_count
    animal_count = animal_count + 1
    return name, sex, generate_unique_id("duck"), age


def cat_cry(cat_properties: tuple):
    name, sex, uid, color = cat_properties
    print(
        f"Hi, I am Cat. My name is {name}. I am a {sex_i2s(sex)} cat."
        f" My ID is {uid}. My color is {color}."
    )


def dog_cry(dog_properties: tuple):
    name, sex, uid, weight = dog_properties
    print(
        f"Hi, I am Dog. My name is {name}. I am a {sex_i2s(sex)} dog."
        f" My ID is {uid}. My weight is {weight}kg."
    )


def duck_cry(duck_properties: tuple):
    name, sex, uid, age = duck_properties
    print(
        f"Hi, I am Duck. My name is {name}. I am a {sex_i2s(sex)} dog."
        f" My ID is {uid}. I am {age} years old."
    )


def main(args):
    cat1 = create_cat("Kitty", 0, "red")
    cat_cry(cat1)
    dog1 = create_dog("Peter", 1, 20)
    dog_cry(dog1)
    duck1 = create_duck("Donald", 0, 3)
    duck_cry(duck1)
    print(f"There are {animal_count} animals in total.")


if __name__ == "__main__":
    main(None)
