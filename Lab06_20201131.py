# 1
def sel_sort(arr,i = 0):

    j = i + 1
    minpos = i

    if i == len(arr):
        return

    while j < len(arr):
        if arr[j]<arr[minpos]:
            minpos = j
        j += 1

    temp = arr[i]
    arr[i] = arr[minpos]
    arr[minpos] = temp
    sel_sort(arr, i+1)

    return arr

arr = [4,3,7,98,1,0]
print(sel_sort(arr))

#2

def insert_sort(arr,n):

    i = arr[n - 1]
    j = n - 2

    if n <= 1:
        return
    insert_sort(arr,n-1)

    while j >= 0 and arr[j] > i:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = i

    return arr

arr = [4,2,6,75,8,1]
n = len(arr)

print(insert_sort(arr,n))

#3 #4 #5

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self,arr):
        self.head = None
        tail = None


        if len(arr) == 0:
            print('Array is empty')
        else:
            for i in arr:
                newNode = Node(i)
                if self.head is None:
                    self.head = newNode
                    tail = newNode
                tail.next = newNode
                tail = newNode

#3
    def bubble_sort(self):
        n = self.head
        while n is not None:
            head = n
            nextn = n.next

            while nextn is not None:
                if head.value > nextn.value:
                    temp = head.value
                    head.value = nextn.value
                    nextn.value = temp
                nextn = nextn.next
            #print(self.head.value,end = ' ')
            n = n.next

#4
    def select_sort(self):
        n = self.head

        while n is not None:
            minpos = n
            next = n.next

            while next is not None:
                if minpos.value > next.value:
                    minpos = next
                next = next.next

            temp = n.value
            n.value = minpos.value
            minpos.value = temp

            n = n.next

    def printList(self):
        n = self.head
        while n is not None:
            print(n.value, end = ' ')
            n = n.next

#5
class DoublyLL:
    def __init__(self,arr):
        self.head = None
        self.tail = None

        for i in arr:
            newNode = Node(i)

            if self.head is None:
                self.head = newNode
                self.tail = newNode
                self.tail.next = None
                self.head.prev = None
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                self.tail.next = None

    def insert_sort(self):
        n = self.head
        if n is None:
            return
        else:
            head = self.head

            while head.next is not None:
                nextt = head.next
                while nextt is not None:
                    if head.value > nextt.value:
                        temp = head.value
                        head.value = nextt.value
                        nextt.value = temp
                    nextt = nextt.next
                head = head.next


    def printList(self):
        n = self.head
        while n is not None:
            print(n.value, end = ' ')
            n = n.next

arr = [20,3,45,7,12,98,31]
LL1 = LinkedList(arr)
LL1.bubble_sort()
LL1.select_sort()
LL1.printList()
print()

arr1 = [23,54,8,1,90,76]
DL1 = DoublyLL(arr1)
DL1.insert_sort()
DL1.printList()
print()
#6

def bin_src(arr,start,end,key):

    if start > end:
        return

    mid = (start + end) // 2

    if key == arr[mid]:
        return f'It\'s at index {mid}'

    if key < arr[mid]:
        return bin_src(arr,start,mid - 1,key)

    return bin_src(arr,mid + 1,end,key)

arr = [1,2,3,4,5]

print(bin_src(arr,0,len(arr)-1,2))

#7

def fib(n):
    fibDict = {1:1,2:1} #manually storing the first and second results

    def fibMem(n,fibDict):

        if n in fibDict:
            return fibDict[n]

        result = fibMem(n-1,fibDict)+fibMem(n-2,fibDict)
        fibDict[n] = result

        return result

    return fibMem(n,fibDict)

print(fib(130))




