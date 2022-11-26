from linked_list import LinkedList


class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, item):
        self.append(item, 0)

    def pop(self):
        self.remove(0)


if __name__ == '__main__':
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.push('d')
    stack.push('e')
    stack.push('f')
    print(stack[0].item)

    stack.pop()
    stack.pop()
    print(stack[0].item)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()