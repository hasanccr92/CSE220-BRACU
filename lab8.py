class Tnode:

    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None

class Tree:

    def makeNode(self,value):
        return Tnode(value)

    def addLeaf(self,node,value):
        if node is None:
            return self.makeNode(value)

        if value < node.value:
            node.left = self.addLeaf(node.left,value)
        else:
            node.right = self.addLeaf(node.right,value)

        return node

#1
    def height(self,root):

        if root is None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1

#2
    def level(self,root,nodeval,sroot = 0):
        if root is None:
            return
        if root.value == nodeval:
            return sroot
        else:
            return self.level(root.left,nodeval,sroot+1) or self.level(root.right,nodeval,sroot+1)

#3
    def preOrder(self,root):
        if root is not None:
            print(root.value,end = ',')
            self.preOrder(root.left)
            self.preOrder(root.right)

#4
    def inOrder(self,root):
        if root is not None:
            self.preOrder(root.left)
            print(root.value, end=',')
            self.preOrder(root.right)
        print()

#5
    def postOrder(self,root):
        if root is not None:
            self.preOrder(root.left)
            self.preOrder(root.right)
            print(root.value, end=',')


###########TESTER############
tree1 = Tree()
root = tree1.makeNode(6)
tree1.addLeaf(root,7)
tree1.addLeaf(root,11)
tree1.addLeaf(root,2)
tree1.addLeaf(root,5)
tree1.addLeaf(root,3)
tree1.addLeaf(root,12)
tree1.addLeaf(root,4)
tree1.addLeaf(root,1)


print('The height of the tree: ',tree1.height(root))
print('Level of node is: ',tree1.level(root,12))
tree1.preOrder(root)
print()
tree1.inOrder(root)
tree1.postOrder(root)

'''
    def chkDuplicate(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None and root1.value == root2.value:
            left = self.chkDuplicate(root1.left, root2.left)
            right = self.chkDuplicate(root1.right, root2.right)
        if left and right:
            return True
        return False

    def copyTree(self,root):
        copyRoot = Tnode(root.value)

        if root.left is not None:
            copyRoot.left = self.copyTree(root.left)
        if root.right is not None:
            copyRoot.right = self.copyTree(root.right)

        return copyRoot
        
    def noNodes():
        if root is None:
            return 0
        else:
            return 1+noNodes(root.left)+noNodes(root.right)
            '''

