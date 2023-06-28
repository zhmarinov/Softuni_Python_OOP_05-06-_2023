from typing import List


class Vet:
    animals: List[str] = []
    SPACE = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name: str):
        if len(self.animals) >= Vet.SPACE:
            return "Not enough SPACE"

        self.animals.append(animal_name)
        Vet.animals.append(animal_name)

        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name: str):
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"
        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)

        return f"{animal_name} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.SPACE - len(Vet.animals)} SPACE left in clinic "


peter = Vet("Peter")
george = Vet("George")

print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))

print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))

print(peter.info())
print(george.info())