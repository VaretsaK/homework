class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} is {self.breed}")


dog_1 = Dog("Fred", "Akita", 3)
dog_2 = Dog("Terner", "Akbash", 12)

dog_1.bark()
dog_2.bark()
