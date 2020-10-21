class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print(self):
        print(self.items)

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(5)
    stack.push(3)
    stack.print()