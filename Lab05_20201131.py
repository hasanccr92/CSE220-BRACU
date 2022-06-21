###########TASK-1#############
# a
def fact(n):

    if n == 0:
        return 1
    else:
        return n*fact(n-1) #recursive case

print(fact(1))

# b
def fib(n):

    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2) #recursive case

print(fib(10))

# c
def printarr(arr,i = 0):

    if i == len(arr):
        return
    else:
        print(arr[i],end =' ')
        printarr(arr,i+1) #recursive case

printarr([1,2,3,4,5])
print()


# d
def powerN(base,power):

    if power == 1:
        return base
    else:
        return base*powerN(base,power-1) #recursive case

print(powerN(3,2))


###########TASK-2#############
# a
def dec_to_bin(n,res = ''):

    if n == 0:
        return res

    res += str(n % 2)
    return dec_to_bin(n//2,res) #recursive case

print(dec_to_bin(5))

# b
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self,arr):

        self.head = None
        tail = None
        for i in arr:
            if len(arr) == 0:
                print('empty array')

            else:
                newNode = Node(i)
                if self.head is None:
                    self.head = newNode
                    tail = newNode

                else:
                    tail.next = newNode
                    tail = newNode

    def add_all(self,n):

        if n is None:
            return 0
        else:
            return n.value + self.add_all(n.next)

# c
    def printRev(self,n):

        if n is None:
            return

        else:
            self.printRev(n.next) #recursive case
            print(n.value,end = ' ')


arr = [1,2,3,4,5]

LL1 = Linked_List(arr)
print(LL1.add_all(LL1.head))
LL1.printRev(LL1.head)

print()


# 3
def hocBuilder(height):

    if height == 0:
        return f'No house to build'

    if height == 1:
        return 8

    else:
        total = 8 + (5 * (height-1))
        hocBuilder(height-1) #recursive case

    return total

print(hocBuilder(3))

# 4
# a
def pattern(n,i = 1):

    if n == 0:
        return None

    else:
        pattern(n-1) #recursive case

        for j in range(n):
            print(i,end = ' ')
            i += 1
        print()

pattern(5)

# b
def right_Pattern(n,i):
    s = ' '

    if n == 0:
        return

    right_Pattern(n-1,i) #recursive case
    print()

    for i in range(i-n):
        print(s,end = ' ')

    for i in range(n):
        print(i+1,end = ' ')

right_Pattern(5,5)
print()

# 5

class FinalQ:

    def printResult(self,array,idx = 0):
        if idx<len(array):
            profit = self.calcProfit(array[idx])
            print(idx + 1, ": Investment:", array[idx], "; Profit: ", profit)

    def calcProfit(self,investment):
        
        if investment == 25000:
            return 0.0
        elif 26000 > investment > 25000:
            return 4.5 + float(self.calcProfit(investment - 100))
        elif 100000 >= investment >= 26000:
            return 45 + float(self.calcProfit(investment - 1000))
        elif 101000 > investment > 100000:
            return 8 + float(self.calcProfit(investment - 100))
        elif investment >= 101000:
            return 80 + float(self.calcProfit(investment - 1000))


array = [25000,100000,250000,350000]
f = FinalQ()
f.printResult(array,2)





