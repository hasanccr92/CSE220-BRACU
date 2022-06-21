#######################TASK-1#########################

def StackList(strr):

    stack1 = []
    pointer = -1

    open = ['(', '{', '[']
    close = [')', '}', ']']

    for i in strr:
        if i in open:
            stack1.append(i)
            pointer += 1
        if i in close:
            outt = stack1.pop()

            if open.index(outt) != close.index(i):
                return f'This expression is NOT correct\nError at character #{exp.index(outt)}. "{outt}" is not closed'

    return f'This expression is correct'

strr = "1+2*(3/4)"

print(StackList(strr))



#######################TASK-2#########################

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class StackLL:
    def __init__(self):
        self.head = None

    def push(self,elm):
        if self.head is None:
            self.head = Node(elm)
        else:
            newNode = Node(elm)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.head is None:
            print('Empty List')
        else:
            temp = self.head.value
            self.head = self.head.next
            return temp

    def parenthesisBalance(self,exp):
        open = ['(', '{', '[']
        close = [')', '}', ']']

        for i in exp:
            if i in open:
                stack2.push(i)
            if i in close:
                if self.head is None:
                    return f'This expression is NOT correct\nError at character #{exp.index(outt)}. {outt} is not closed'
                outt = stack2.pop()
                if open.index(outt) != close.index(i):
                    return f'This expression is NOT correct\nError at character #{exp.index(outt)}. "{outt}" is not closed'

        return f'This expression is correct'

exp = "1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
stack2 = StackLL()

print(stack2.parenthesisBalance(exp))
