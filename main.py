class Queue:
    def __init__(self,size):
        self.queue = [None]*size
        self.front= 0
        self.rear = 0 #back item in the queue, last item
        self.size= size
        self.available = size

    def enqueue(self,item):
        if self.available==0:
            print("Queue is overloaded")
        else:
            self.queue[self.rear] = item
            self.rear=(self.rear+1) % self.size # the modulus (%) is basically giving u the remainder when doing the divison 
            self.available -=1

    def dequeue(self):
        if self.available == self.size:
            print("Queue is underflowed")
        else: #adding more spaces in the queue 
            self.queue[self.front] = None
            self.front=(self.front+1) % self.size  
            self.available +=1

    def getfront(self):
        print(self.queue[self.front])

    def getrear(self):
        print(self.queue[self.rear])

    def print_queue(self):
        print(self.queue)


#testing examples
q = Queue(4) #size of queue  is 4
q.enqueue(5)
q.enqueue(6)
q.enqueue(8)
q.enqueue(10)
q.print_queue()
q.dequeue()
q.print_queue()
q.getfront()
q.getrear()






    


        


