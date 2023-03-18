class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"The dog's name is {self.name}, the breed {self.breed}")


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"It's {self.name}, I'm {self.age} years old!"

    def add_dog(self, dog):
        if not isinstance(dog, Dog):
            raise "No such dogs were found."
        self.dog = dog


dog_1 = Dog("Fred", "Akita", 3)

person_1 = Person("Rick", 23, "Male")
person_1.add_dog(dog_1)

print(person_1)
person_1.dog.bark()
