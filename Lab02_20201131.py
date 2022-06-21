#######################TASK-1#########################

# i)
class Node:

    def __init__(self,value,next):
        self.value = value
        self.next = None

# ii)
class MyList:

    #######################TASK-2#########################

    def __init__(self,a):
        self.head = None
        tail = None


        if len(a) == 0:
            print('Array is empty')
        else:
            for i in a:
                newNode = Node(i,None)
                if self.head is None:
                    self.head = newNode
                    tail = newNode
                tail.next = newNode
                tail = newNode

    #2
    def showList(self):

        n = self.head
        if n is None:
            print('Empty List')
        else:
            while (n is not None):
                print(n.value,end = '->')
                n = n.next
        print()

    #3
    def isEmpty(self):

        n = self.head
        if n is None:
            print(True)
        else:
            print(False)

    #4
    def clear(self):

        n = self.head

        if n is None:
            print('Empty List')
        else:
            self.head = None


    #5
    def insertTail(self,newElement):

        n = self.head
        flag = False
        newNode = Node(newElement,None)

        while n is not None:
            if n.value == newElement:
                print('Element already exists')
                flag = True
            n = n.next

        if flag == False:
            if n == None:
                n = newNode
            else:
                while n.next is not None:
                    n = n.next
                n.next = newNode

    #6
    def insertAt(self,newElement,index):

        n = self.head
        newNode = Node(newElement,None)
        c = 0
        flag = False

        if n is None:
            print('Empty List')
            return

        while n is not None:
            if n.value == newElement:
                print('Element already exists')
                flag = True
            if c == index - 1:
                prevNode = n
            n = n.next
            c += 1

        if flag == False:
            if index<0 or index>c:
                print('Invalid index')
            else:
                if index == 0:
                    newNode.next = self.head
                    self.head = newNode
                else:
                    newNode.next = prevNode.next
                    prevNode.next = newNode

    #7
    def remove(self,deletekey):

        n = self.head

        if n is None:
            print('Empty List')
            return

        if deletekey == n.value:
            self.head = n.next
            print(deletekey)
        else:
            while n.next is not None:
                if n.next.value == deletekey:
                    break
                n = n.next

            if n.next is None:
                print('deletekey is not in Linked List')
            else:
                n.next = n.next.next
                print(deletekey)


#######################TASK-3#########################

    #1
    def evens(self):

        n = self.head
        copyHead = None
        copyTail = None

        while n is not None:
            if (n.value)%2 == 0:
                newNode = Node(n.value, None)

                if copyHead == None:
                    copyHead = newNode
                    copyTail = newNode
                else:
                    copyTail.next = newNode
                    copyTail = newNode

                print(copyTail.value)
            n = n.next

    #2
    def findElm(self,elm):

        n = self.head
        flag = False

        while n is not None:
            if elm == n.value:
                flag = True
            n = n.next
        print(flag)

    #3
    def reverseList(self):

        n = self.head
        revHead = None

        while n is not None:
            nextN = n.next
            n.next = revHead
            revHead = n
            n = nextN
        self.head = revHead


    #4
    def sortLL(self):

        n = self.head
        nextN = None

        while n is not None:
            nextN = n.next

            while nextN is not None:
                if n.value>nextN.value:
                    n.value,nextN.value = nextN.value,n.value
                nextN = nextN.next
            n = n.next

    #5
    def summation(self):

        n = self.head
        c = 0

        while n is not None:
            c += n.value
            n = n.next

        print(c)

    #6
    def rotateList(self,dir,k):

        if dir.lower() == 'left':

            for i in range(k):
                prevHead = self.head
                self.head = self.head.next
                tail = self.head

                while tail.next is not None:
                    tail = tail.next
                tail.next = prevHead
                prevHead.next = None

        if dir.lower() == 'right':

            n = self.head
            revHead = None

            while n is not None:
                nextN = n.next
                n.next = revHead
                revHead = n
                n = nextN
            self.head = revHead

            for i in range(k):

                prevHead = self.head
                self.head = self.head.next
                tail = self.head

                while tail.next is not None:
                    tail = tail.next
                tail.next = prevHead
                prevHead.next = None








arr = [10,31,21,40,50]

LL1 = MyList(arr)

LL1.sortLL()

LL1.showList()

LL1.isEmpty()

LL1.insertTail(100)

LL1.showList()

LL1.insertAt(100,4)

LL1.remove(100)

LL1.evens()

LL1.findElm(1)

LL1.reverseList()

LL1.sortLL()

LL1.summation()

LL1.rotateList('left',2)

LL1.showList()

LL1.clear()

