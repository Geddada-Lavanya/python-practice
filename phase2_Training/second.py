#  Invalid Position of give input else return -1


# def isValid(s):
#     stack=[]
#     for i in range(len(s)):
#         if s[i]=="(":
#             stack.append(")")
#         elif s[i]=="{":
#             stack.append("}")
#         elif s[i]=="[":
#             stack.append("]")
#         else:
#             if len(stack)==0:
#                 return i+1
#             n=stack.pop()
#             if n!=s[i]:
#                 return i+1
#     if not stack:
#         return -1
#     return len(s)+1
# s=input()
# print(isValid(s))



#Singly Linked list example playlist 

# class Song:
#     def __init__(self,s_name):
#         self.s_name=s_name
#         self.n_song_ad=None

# class Playlist:
#     def __init__(self):
#         self.f_song=None

#     def add_songs(self,song_n):
#         new_song=Song(song_n)
#         if self.f_song is None:
#             self.f_song=new_song
#             return 
#         temp=self.f_song
#         while(temp.n_song_ad!=None):
#             temp=temp.n_song_ad
#         temp.n_song_ad=new_song

#     def display(self):
#         if self.f_song is None:
#             return 
#         curr=self.f_song
#         while curr != None:
#             print(curr.s_name,end="->")
#             curr=curr.n_song_ad
#         print("None")

# p=Playlist()
# p.add_songs("rrr")
# p.add_songs("hi nanna")
# p.add_songs("kgf")
# p.display()




# standard code for singly linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class sll:
#     def __init__(self):
#         self.head=None
#     def insert(self,data):
#         new_n=Node(data)
#         if self.head is None:
#             self.head=new_n
#             return
#         curr=self.head
#         while(curr.next):
#             curr=curr.next
#         curr.next=new_n
#     def display(self):
#         if self.head is None:
#             print('List is empty')
#         curr_n=self.head
#         while(curr_n!=None):
#             print(curr_n.data,end=' -> ')
#             curr_n=curr_n.next
#         print(None)
#     def insert_at_index(self,ind,data):
#         new_n=Node(data)
#         pos=0
#         if(pos==ind):
#             new_n.next=self.head
#             self.head=new_n
#             return
#         curr=self.head
#         while(pos+1!=ind and curr!=None):
#             pos+=1
#             curr=curr.next
#         if(pos+1==ind):
#             new_n.next=curr.next
#             curr.next=new_n
#     def delete_at_index(self,ind):
#         pos=0
#         if(self.head is None):
#             return 
#         if(pos==ind):
#             self.head=self.head.next
#             return 
#         curr=self.head
#         while(pos+1!=ind and curr!=None ):
#             pos+=1
#             curr=curr.next
#         if(pos+1==ind and curr.next!=None):
#             curr.next=curr.next.next
# o=sll()
# o.insert("rrr")
# o.insert("kgf")
# o.insert("hi_nanna")
# o.display()
# o.insert_at_index(1,"oopiri")
# o.display()
# o.delete_at_index(1)
# o.display()

# https://www.hackerrank.com/contests/fundamentals-of-programming/challenges

    
