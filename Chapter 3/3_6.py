from queue import Queue

class Animal(object):
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.order = 0
class Animal_Queue(object):
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()
        self.time = 0
    
    def enqueue(self, animal):
        animal.order = self.time
        self.time += 1

        if animal.kind == 'dog':
            self.dog_queue.add(animal)
        else:
            self.cat_queue.add(animal)

    def dequeue_any(self):
        if self.dog_queue.front().order < self.cat_queue.front().order:
            self.dog_queue.remove()
        else:
            self.cat_queue.remove()
    
    def dequeue_dog(self):
        self.dog_queue.remove()

    def dequeue_cat(self):
        self.cat_queue.remove()

    def print_animal_queue(self):
        print '[',
        for i in range(self.dog_queue.size):
            print self.dog_queue.list[i].name,
        print ']'
        
        print '[',
        for i in range(self.cat_queue.size):
            print self.cat_queue.list[i].name,
        print ']'


def main():
    animal_1 = Animal('A', 'dog')
    animal_2 = Animal('B', 'cat')
    animal_3 = Animal('C', 'cat')
    animal_4 = Animal('D', 'cat')
    animal_5 = Animal('E', 'dog')
    animal_6 = Animal('F', 'cat')
    animal_7 = Animal('G', 'dog')
    animal_8 = Animal('H', 'dog')

    animals = Animal_Queue()
    
    animals.enqueue(animal_1)
    animals.enqueue(animal_3)
    animals.enqueue(animal_2)
    animals.enqueue(animal_5)
    animals.enqueue(animal_4)
    animals.enqueue(animal_6)
    animals.enqueue(animal_8)
    animals.enqueue(animal_7)

    animals.print_animal_queue()
    
    animals.dequeue_any()
    animals.print_animal_queue()

    animals.dequeue_dog()
    animals.print_animal_queue()

    animals.dequeue_cat()
    animals.print_animal_queue()

if __name__ == '__main__':
    main()
