#######################TASK-1#########################
# i)
class Node:
    def __init__(self,value):
        self.next = None
        self.prev = None
        self.value = value

# ii)
class DoublyList:

#######################TASK-2#########################
    #1
    def __init__(self,a):
        self.a = a
        self.head = Node('dummy')
        self.head.next = self.head.prev = self.head

        if len(a) == 0:
            print('Empty Array')

        for i in a:
            newNode = Node(i)

            if self.head is None:
                self.head = newNode
                newNode.next = self.head
                newNode.prev = self.head
            else:
                newNode.prev = self.head.prev
                newNode.next = self.head
                self.head.prev.next = newNode
                self.head.prev = newNode

    #2
    def showList(self):
        n = self.head.next

        if n is None:
            return ('Empty List')

        while n.next is not self.head:
            print(n.value,end = '<->')
            n = n.next

        print(n.value)

    #3
    def insertTail(self,newElement):
        n = self.head.next
        flag = True

        if n is None:
            return 'List is empty'

        while n.next is not self.head:
            if n.next.value == newElement:
                print('Element already exists')
                flag = False
            n = n.next

        if flag == True:
            newNode = Node(newElement)
            self.tail = self.head.prev
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = self.head

    #4
    def insertAt(self,newElement,index):
        n = self.head.next
        flag = True
        count = 0

        if n is None:
            return 'List is empty'

        while n.next is not self.head:
            if n.next.value == newElement:
                print('Element already exists')
                flag = False
            if count == index - 1:
                prevNode = n
            count += 1
            n = n.next

        if index<0 or index > count:
            return ('Invalid index')

        if flag == True:
            newNode = Node(newElement)
            n = self.head.next
            newNode.next = prevNode.next
            prevNode.next = newNode


    #5
    def remove(self,index):
        count = 0
        n = self.head.next

        if n is None:
            return 'Empty list'

        while n.next is not self.head:
            if count == index-1:
                prevNode = n
            count += 1
            n = n.next

        if index<0 or index>count:
            return 'Invalid index'

        prevNode.next = prevNode.next.next

    #6
    def removeKey(self,deletekey):
        n = self.head.next

        if n is None:
            return 'Empty List'
        
        while n.next is not self.head:
            if n.next.value == deletekey:
                delnode = n.next
            n = n.next

        delnode.prev.next = delnode.next
        print(delnode.value)




a = [10,20,30,40,50]

DL1 = DoublyList(a)

DL1.showList()

DL1.insertTail(50)

DL1.showList()

DL1.insertAt(9,2)

DL1.showList()

DL1.remove(2)

DL1.showList()

DL1.removeKey(20)

DL1.showList()
