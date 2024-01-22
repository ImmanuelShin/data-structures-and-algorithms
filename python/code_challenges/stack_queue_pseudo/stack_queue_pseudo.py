from code_challenges.stack_and_queue.stack_queue import Stack


class PseudoQueue:
    
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        if self.stack1.is_empty():
            self.stack1.push(value)
        else:
            while self.stack1.is_empty() == False:
                self.stack2.push(self.stack1.pop())

            self.stack1.push(value)

            while self.stack2.is_empty() == False:
                self.stack1.push(self.stack2.pop())


    def dequeue(self):
        if self.stack1.is_empty():
            raise IndexError("There's nothing here")
        return self.stack1.pop()