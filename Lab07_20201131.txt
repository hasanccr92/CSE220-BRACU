#TASK-1
class KeyIndex:
    def __init__(self, a):
        self.a = a
        self.maxx = max(self.a)
        self.minn = min(self.a)
        if self.minn < 0:
            self.k = [0] * (1 + (2 * self.maxx))
        else:
            self.k = [0] * (self.maxx + 1)

    # POPULATING THE ARRAY
        for i in self.a:
            if self.minn < 0:
                self.k[i + (abs(self.minn))] += 1
            else:
                self.k[i] += 1
        print('Auxilliary Array: ',self.k)

    def search(self, key):

        if key > len(self.k) or key > (len(self.k) + abs(self.minn)):
            return False
        else:
            if self.minn < 0:
                return self.k[key + abs(self.minn)] != 0

            else:
                return self.k[key] != 0

    def sort(self):
        i = 0
        k = 0
        arr = [0] * len(self.a)
        if self.minn >=0:
            for i in range(len(self.k)):
                while self.k[i] > 0:
                    arr[k] = i
                    self.k[i] = self.k[i] - 1
                    k += 1
            return arr
        else:
            for i in range(len(self.k)):
                while self.k[i] > 0:
                    arr[k] = i - abs(self.minn)
                    self.k[i] = self.k[i] -1
                    k += 1
            return arr



#####TESTER#####
a = [2, 4, 6, -1,5, -1,1]
Key1 = KeyIndex(a)
print(Key1.search(8))
print(Key1.sort())

#TASK-2
def hashTable(arr):
    hashArr = [None]*len(arr)
    vowels = [65,69,73,79,85]
    digits = []
    for i in range(48, 58):
        digits.append(i)
    consCount = 0
    digSum = 0

    for i in arr:
        if ord(i) not in vowels and ord(i) not in digits:
            consCount += 1
        if ord(i) in digits:
            digSum += int(i)

    hashValue = (consCount*24)+digSum
    hashInd = hashValue % 9

    print('Index:',hashInd)

    if hashArr[hashInd] is None:
        hashArr[hashInd] = arr
    else:
        while True:
            hashInd = (hashInd + 1) % len(hashArr)
            if hashArr[hashInd] is None:
                hashArr[hashInd] = arr
            break
    print(hashArr)
print()
hashTable('ST1E89B8A32')

