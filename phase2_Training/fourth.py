class Tree_Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        self.q=[]
    def insert(self,data,root):
        if root == None:
            return Tree_Node(data)
        if data<root.data:
            root.left=self.insert(data,root.left)
        elif data>root.data:
            root.right=self.insert(data,root.right)
        return root
    def in_order(self,root):
        if root == None:
            return 
        self.in_order(root.left)
        print(root.data,end=" ")
        self.in_order(root.right)
    def pre_order(self,root):
        if root==None:
            return 
        print(root.data,end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)
    def post_order(self,root):
        if root==None:
            return 
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data,end=" ")
    def level_order(self,root):
        if not root:
            return
        self.q.append(root)
        while len(self.q)!=0:
            temp=self.q.pop(0)
            print(temp.data,end=" ")
            if temp.left:
                self.q.append(temp.left)
            if temp.right:
                self.q.append(temp.right)
        
o=BST()
while True:
    a=int(input())
    if a<0:
        break
    o.root=o.insert(a,o.root)
o.in_order(o.root)
print()
o.pre_order(o.root)
print()
o.post_order(o.root)
print()
o.level_order(o.root)
