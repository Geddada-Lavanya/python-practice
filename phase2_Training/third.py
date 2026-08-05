class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Dll:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
        new_node.prev=curr
    def forward_traversal(self):
        if self.head==None:
            return 
        curr=self.head
        while curr!=None:
            print(curr.data,end="->")
            curr=curr.next
        print("None")
    def backward_traversal(self):
        if self.head==None:
            return 
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        while(curr!=None):
            print(curr.data,end="->")
            curr=curr.prev
        print("None")
    def insert_at_index(self,ind,data):
        new_n=Node(data)
        if self.head is None:
            return 
        pos=0
        curr=self.head
        if(pos==ind):
            new_n.next=self.head
            self.head=new_n
            if curr!=None:
                new_n.next.prev=new_n
            return 
        
        
        







class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class scll:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_n=Node(data)
        if self.head is None:
            self.head=new_n
            new_n.next=new_n
            return
        curr=self.head
        while(curr.next!=self.head):
            curr=curr.next
        curr.next=new_n
        new_n.next=self.head
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        curr_n=self.head
        while(curr_n!=self.head):
            print(curr_n.data,end=' -> ')
            curr_n=curr_n.next
        print(curr_n.data)
    # def insert_at_index(self,ind,data):
    #     new_n=Node(data)
    #     pos=0
    #     if(pos==ind):
    #         new_n.next=self.head
    #         self.head=new_n
    #         return
    #     curr=self.head
    #     while(pos+1!=ind and curr!=None):
    #         pos+=1
    #         curr=curr.next
    #     if(pos+1==ind):
    #         new_n.next=curr.next
    #         curr.next=new_n
    # def delete_at_index(self,ind):
    #     pos=0
    #     if(self.head is None):
    #         return 
    #     if(pos==ind):
    #         self.head=self.head.next
    #         return 
    #     curr=self.head
    #     while(pos+1!=ind and curr!=None ):
    #         pos+=1
    #         curr=curr.next
    #     if(pos+1==ind and curr.next!=None):
    #         curr.next=curr.next.next
o=scll()
o.insert("rrr")
o.insert("kgf")
o.insert("hi_nanna")
o.display()
# o.insert_at_index(1,"oopiri")
# o.display()
# o.delete_at_index(1)
# o.display()







class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class dcll:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_n = Node(data)

        if self.head is None:
            self.head = new_n
            new_n.next=self.head
            new_n.prev=self.head
            return
        curr = self.head
        while curr.next!=self.head:
            curr = curr.next
        curr.next = new_n
        new_n.prev = curr
        new_n.next=self.head
        self.head.prev=new_n

    def forward(self):
        if self.head is None:
            print("List is empty")
            return

        curr = self.head
        print(curr.data,end="<o>")
        curr=curr.next
        while curr!=self.head:
            print(curr.data, end="<o>")
            curr = curr.next
        print(curr.data)

    def backward(self):
        if self.head is None:
            print("List is empty")
            return

        curr = self.head
        while curr.next!=self.head:
            curr = curr.next
        last=curr
        print(curr.data,end="<o>")
        curr=curr.prev
        while curr!=last:
            print(curr.data, end="<o>")
            curr = curr.prev
        print(curr.data)
o = dcll()
print("Enter numbers:")
while True:
    a = int(input())
    if a < 0:
        break
    o.insert(a)
o.forward()
o.backward()