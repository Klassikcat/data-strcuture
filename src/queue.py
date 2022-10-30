from linked_list import LinkedList


class Queue(LinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, item):
        self.append(item, 0)

    def dequeue(self):
        self.remove(self.__len__() - 1)
