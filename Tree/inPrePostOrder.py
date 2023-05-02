class Node:
    def __init__(self,value,previous=None,next=None):
        self.value=value
        self.previous=previous
        self.next=next

    def __str__(self):
        return f"The value is {self.value} and previous pointer is {self.previous} and next pointer is {self.next}"
    

class Tree:
    def __init__(self):
        self.head=None
  
    def showNode(self):
        t=self.head
        while t:
            print(t.value)
            t=t.next
    
    def inorder(self,t):
        if t:
            self.inorder(t.previous)
            print(t.value , end=' ')
            self.inorder(t.next) 

    def preorder(self,t):
        if t:
            print(t.value , end=' ')
            self.preorder(t.previous)
            self.preorder(t.next)  
            
    def postorder(self,t):
        if t:
            self.postorder(t.previous)
            self.postorder(t.next)  
            print(t.value , end=' ')
    
    def doubleorder(self,t):
        if t:
            print(t.value , end=' ')
            self.doubleorder(t.previous)
            print(t.value , end=' ')
            self.doubleorder(t.next)  
    
    def tripleorder(self,t):
        if t:
            print(t.value , end=' ')
            self.tripleorder(t.previous)
            print(t.value , end=' ')
            self.tripleorder(t.next)  
            print(t.value , end=' ')
    
    def indirect1(self,t):
        if t:
            print(t.value,end=' ')
            self.indirect2(t.previous)
            self.indirect2(t.next)
        
    def indirect2(self,t):
        if t:
            self.indirect1(t.previous)
            print(t.value , end=' ')
            self.indirect1(t.next)

    
    
        
       
     


n1=Node('A')
n1.previous=Node('B')
n1.next=Node('C')
n1.previous.previous=Node('D')
n1.previous.next=Node('E')
n1.next.previous=Node('F')
n1.next.next=Node('G')


        
t1=Tree()
t1.head=n1
t1.showNode()
print("Inorder is : -" ,end=' ' )
t1.inorder(n1)
print()
print("Preorder is : -" , end=' '  )
t1.preorder(n1)
print()
print("Postorder is : -" ,end=' ' )
t1.postorder(n1)
print()
print("Double Order is : -" ,end=' ' )
t1.doubleorder(n1)
print()
print("Triple Order is : -" ,end=' ' )
t1.tripleorder(n1)
print()
print("Indirect Value  is : -" ,end=' ' )
t1.indirect1(n1)