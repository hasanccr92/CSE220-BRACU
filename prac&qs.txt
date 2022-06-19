def printreverse(s, i, c):
    vowel = "AEIOUaeiou"
    new_s = ""
    for j in s:
        if j in vowel:
            new_s += j
            c += 1

    def reverse(string):
        if len(string) == 0:
            return
        temp = string[0]
        #i = c+1
        reverse(string[1:])
        print(temp, end='')
    reverse(new_s)
    print()
    print("Count is", c)


printreverse("Axe3*8E7U9Ve1%", 0, 0)

def firstFunc(arr,index1,index2,maxx):
    index2 += 1

    if index2>=len(arr[index1]):
        index2 = 0
        index1 += 1
    if index1 == len(arr):
        return maxx
    else:
        val = arr[index1][index2]
        if int(val) > maxx:
            maxx = val
        return firstFunc(arr,index1,index2,maxx)


ar = [[15,18],[4,17]]
print(firstFunc(ar,0,0,ar[0][0]))

def reverseMixed(s1,s2,i1,i2,c=0):
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    i1 = 0
    i2 = len(s2)-1
    for i in s1:
        if i in vowels:
            c+=1
    for i in s2:
        if i in vowels:
            c+=1


    def mixStr(s1,s2,i1,i2):
        new_s = ''
        if i1>len(s1)-1 or i2<0:
            return new_s

        temp1 = s1[0]
        temp2 = s2[-1]
        new_s += (temp2+temp1)

        return mixStr(s2[i2],s1[i1],i2-1,i1+1)

    print('Count is: ', c)
    #mixStr(s1, s2,i1,i2)

print(reverseMixed('ABcdd','weXyZ',0,0))

def string_len(str1):
    if len(str1) == 0:
        return 0
    else:
        return 1+string_len(str1[1:])
print(string_len('12345'))


def str_rev(arr):

    if arr == '':
        return ''
    return str_rev(arr[1:])+arr[0]

print(str_rev('mystr'))

def palChk(strr):

    if len(strr) == 0 or len(strr) == 1:

        return True
    if strr[0] == strr[len(strr)-1]:
        return palChk(strr[1:-1])

    return False
print(palChk('kayak'))

def dec_to_bin(num,summ = ''):
    if num == 0:
        return summ
    else:
        summ += str(num%2)
        return dec_to_bin(num//2,summ)
print(dec_to_bin(21))

def bin_to_dec(num,i = 0,dec = 0):
    if len(str(num)) == i:
        return dec
    if num[i] == '0':
        dec = dec * 2
    else:
        dec = dec*2+1
    return bin_to_dec(num,i+1,dec)
print(bin_to_dec('101'))


def sumofNum(n):
    if n == 0:
        return n
    return n+sumofNum(n-1)
print(sumofNum(10))

def fibb(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)
print(fibb(5))

def sumOfDigits(num):
    if num == 0:
        return 0

    return (num%10 + sumOfDigits(num//10))
print(sumOfDigits(123))

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#LL recursion
class Node:

    def __init__(self,value,next):
        self.value = value
        self.next = None


class MyList:

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

    def showList(self):

        n = self.head
        if n is None:
            print('Empty List')
        else:
            while (n is not None):
                print(n.value,end = '->')
                n = n.next
        print()
    def revRec(self,node):

        if (node.next == None):
            self.head = node
            return

        self.revRec(node.next)
        temp = node.next
        temp.next = node
        node.next = None


    def length(self,node):
        if node is None:
            return 0
        else:
            return 1+self.length(node.next)


arr = [1,2,3,4,5]
LL1 = MyList(arr)
LL1.revRec(LL1.head)
print(LL1.length(LL1.head))
LL1.showList()


def printFwd(arr):
    if len(arr) == 0:
        return
    else:
        print(arr[0], end=',')
        printFwd(arr[1:])


arr = [2,3,45,6,1]
printFwd(arr)

