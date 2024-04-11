class Stack:
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)   

    def pop(self):
        if self.items:
         return self.items.pop() 
        else:
          return None

    def peek(self): 
       if self.items:
          return self.items[-1]
       else:
          return None
       
    def is_empty(self):
       return not self.items


class Queue:
    def __init__(self):
       self.stack1=Stack()
       self.stack2=Stack()

    def enqueue(self,item):
       self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        a = self.stack2.pop()
        return a

def main():
    q = Queue()
    input1 = 0

    while input1 != -1:
        input1 = int(input("Enter 1 to push, 2 to pop, -1 to exit\n"))

        if input1 == 1:
            push_value = int(input("Enter number"))
            q.enqueue(push_value)

        if input1 == 2:
            a = q.dequeue()
            print(a)

if __name__ == "__main__":
    main()
