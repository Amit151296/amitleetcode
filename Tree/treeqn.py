
class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

    def __str__(self):
        return f"The value is {self.value} and left pointer is {self.left} and right pointer is {self.right}"
    

class Tree:
    def __init__(self):
        self.head=None
    
    def totalNode(self,t):
        if t:
            return 1+ self.totalNode(t.left) + self.totalNode(t.right)
        return 0

    def leafNode(self,t):
        if t==None: return 0
        if t.left==None and t.right==None :
            return 1
        else:
            return self.leafNode(t.left) + self.leafNode(t.right)

    def noneLeafNode(self,t):
        if t==None: return 0
        if t.left==None and t.right==None :
            return 0
        return 1+self.noneLeafNode(t.left) + self.noneLeafNode(t.right)
    
    def heightOfTree(self,t):
        if t==None: return 0
        if t.left==None and t.right==None:
            return 0
        return 1 + max(self.heightOfTree(t.left),self.heightOfTree(t.right))
    
    def fullNode(self,t):
        if t==None: return 0
        if t.left==None and t.right==None:
            return 0
        if t.left==None and t.right !=None:
            return self.fullNode(t.right)
        if t.left!=None and t.right ==None:
            return self.fullNode(t.left)
        return 1 + self.fullNode(t.left) + self.fullNode(t.right)
        
        
    
    






        

n1=Node('A')
n1.left=Node('B')
n1.right=Node('C')
n1.left.left=Node('D')
n1.left.right=Node('E')
n1.right.left=Node('F')
n1.right.right=Node('G')
n1.left.left.left=Node('H')
n1.left.left.right=Node('I')
n1.left.right.left=Node('J')

# print(n1)
t=Tree()
print('Total Node is :-', end=' ')
print(t.totalNode(n1))
print('Leaf Node is :-',end='')
print(t.leafNode(n1))
print('Non Leaf Node is :-',end='')
print(t.noneLeafNode(n1))
print('Height of Tree is :-',end='')
print(t.heightOfTree(n1))
print('Number of Full Node in the Tree is :-',end='')
print(t.fullNode(n1))

