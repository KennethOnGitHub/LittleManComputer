class CircularQueue():
    def __init__(self, queueSize: int) -> None:
        self.queue = [None for i in range(queueSize)]
        self.head: int = 0
        self.tail:int = 0

        self.max_size = queueSize
        self.size = 0
    
    def enqueue(self, val) -> None:
        self.queue[self.tail] = val
        self.size += 1
        self.tail += 1
        self.tail = self.tail % self.max_size
    
    def dequeue(self):
        self.head += 1
        self.head = self.head % self.max_size
        self.size -= 1
        return self.queue[self.head - 1]
