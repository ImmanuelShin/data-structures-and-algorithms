from code_challenges.stack_and_queue.stack_queue import Stack, Queue


class AnimalShelter:
    def __init__(self):
        self.animals = Queue()
        self.cats = Queue()
        self.dogs = Queue()
    
    def enqueue(self, animal):
        self.animals.enqueue(animal)
        if animal.species == 'cat':
            self.cats.enqueue(animal)
        elif animal.species == 'dog':
            self.dogs.enqueue(animal)
        else:
            raise TypeError("We only hold cats and dogs here")

    def dequeue(self, pref):
        if pref not in ['dog', 'cat']:
            return None

        species_queue = self.dogs if pref == 'dog' else self.cats
        if species_queue.is_empty():
            raise ValueError(f"There ain't no {pref} in here.")
        
        target = species_queue.dequeue()
        target_id = id(target)
        temp = Queue()

        while not self.animals.is_empty():
            animal = self.animals.dequeue()
            if id(animal) != target_id:
                temp.enqueue(animal)
        self.animals = temp
        
        return target
        
class Dog:
    def __init__(self, name=None):
        self.species = 'dog'
        self.name = name
    @staticmethod
    def the_dog_goes():
        print("Woof")
    def __str__(self):
        return f"Dog: {self.name}"
    def __repr__(self):
        return f"Dog('{self.name}')"

class Cat:
    def __init__(self, name=None):
        self.species = 'cat'
        self.name = name
    @staticmethod
    def the_cat_goes():
        print("Meow")
    def __str__(self):
        return f"Cat: {self.name}"
    def __repr__(self):
        return f"Cat('{self.name}')"
