#Problem Statement: https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2= []

    
    def peek(self):

        if len(self.stack2)!=0:
            return self.stack2[-1]
        else:
            while len(self.stack1)!=0:
                x=self.stack1.pop()
                self.stack2.append(x)
            
            return self.stack2[-1]

    
    def pop(self):
        if len(self.stack1)==0 and len(self.stack2)==0:
            return "Stack is empty" 

        if len(self.stack2)!=0:
            self.stack2.pop()
        else: 
            
            while len(self.stack1)!=0:
                x=self.stack1.pop()
                self.stack2.append(x)
            self.stack2.pop()

        
        
    def put(self, value):

        self.stack1.append(value)


        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
