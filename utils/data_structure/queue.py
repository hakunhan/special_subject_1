class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print(self):
        print(self.items)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(7)
    queue.enqueue(5)
    queue.print()