from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal, price):
        is_budget_enough = self.__budget >= price
        is_animal_capacity = self.__animal_capacity > len(self.animals)

        if is_budget_enough and is_animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif is_animal_capacity and not is_budget_enough:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            # worker = next(filter(lambda worker: worker.name == worker_name, self.workers))
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = sum([w.salary for w in self.workers])
        if sum_of_salaries <= self.__budget:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money_for_care = sum([a.money_for_care for a in self.animals])

        if self.__budget >= needed_money_for_care:
            self.__budget -= needed_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"
        lions = [a for a in self.animals if a.__class__.__name__ == "Lions"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions: \n"
        for l in lions:
            result += f"{l}\n"

        result += f"----- {len(tigers)} Tigers: \n"
        for t in tigers:
            result += f"{t}\n"

        result += f"----- {len(cheetahs)} Cheetahs: \n"
        for c in cheetahs:
            result += f"{c}\n"
        return result[:-1]

    def workers_status(self):
        result = result = f"You have {len(self.workers)} animals"
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretakers"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vets"]

        result += f"----- {len(keepers)} Keepers: \n"
        for k in keepers:
            result += f"{k}\n"

            result += f"----- {len(caretakers)} Caretakers: \n"
        for c in caretakers:
            result += f"{c}\n"

            result += f"----- {len(vets)} Vets: \n"
        for v in vets:
            result += f"{v}\n"

        return result[:-1]






























