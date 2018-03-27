class queue:
    def __init__(self):
        self.en = []
        self.de = []

    def enqueue(self, data):
        self.en.append(data)

    def dequeue(self):
        if len(self.de) == 0:
            self.build_dequeue()
        return self.de.pop()

    def build_dequeue(self):
        while len(self.en) > 0:
            self.de.append(self.en.pop())


q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
