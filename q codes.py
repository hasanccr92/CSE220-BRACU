def enqueue(x):
    front = -1
    rear = -1
    array = []
    #if size == len(array)-1:
        #print('Queue overflow')
    if front and rear == -1:
        front = rear = 0
        array[rear] = x
    rear = (rear+1)%len(array)

    array[rear] = x

def dequeue():
    front = -1
    rear = -1
    array = []

    if len(array) == 0:
        print('Queue underflow')
    if front == rear:
        front = rear = -1
    temp = array[front]
    front = (front+1) % len(array)
    return temp

def peek():
    return front

'''Linked List based queues'''
def enqueue(x):
    if front is None and rear is None:
        front = rear = Node(x,None)
    temp = Node(x.None)
    rear.next = temp
    rear = temp
def dequeue():
    if head is None:
        print('Underflow')
    if front == rear:
        front = rear =None
    removed = front
    front = front.next
    removed.next = None
    return removed.value

def peek():
    return front.value

