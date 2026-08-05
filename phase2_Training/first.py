#1) given a float number convert that into 2 numbers after decimal
#Example
# a=8.6467
# ouput=> a=8.64


# a=float(input())
# print(f"{a:.2f}") # 8.65(round figure)

# import math
# a=float(input())
# a=math.floor(a*100)/100
# print(a)




# n = 5
# m = 5
# a = int(input())
# lst = []
# num = 1

# for i in range(n):
#     for j in range(m):
#         if i==0 or j==0 or j==m-1:
#             lst.append(num)
#         num += 1

# if a in lst:
#     print("yes")
# else:
#     print("no")




# n=int(input())
# bc=int(input())
# gm=list(map(int,input().split()))
# bus_cnt=0
# w_hall=0
# for i in range(n):
#     if(gm[i]+w_hall>bc):
#         bus_cnt+=1
#         w_hall=gm[i]
#     else:
#         w_hall+=gm[i]
# if w_hall>0:
#     bus_cnt+=1
# print("Required buses:",bus_cnt)

    

# class Stack:
#     def __init__(self,capacity):
#         self.st=[None]*capacity
#         self.capacity=capacity
#         self.size=0
#         self.top=-1
#     def push(self,data):
#         if self.size==self.capacity:
#             print("stack overflow")
#             return 
#         self.top+=1
#         self.st[self.top]=data
#         self.size+=1
#     def pop(self):
#         if self.size==0:
#             print("Stack underflow")
#             return 
#         deleted=self.st[self.top]
#         self.top-=1
#         self.size-=1
#         print("element deleted",deleted)
#     def print(self):
#         if self.size==0:
#             print("Stack Empty")
#         i=self.top
#         while i>=0:
#             print(self.st[i],end=" ")
#             i-=1
# capacity=int(input())
# o=Stack(capacity)
# while True:
#     a=int(input())
#     if a==-1:
#         break
#     o.push(a)    # while entering numbers into stack if it full then we have to enter -1 for exiting from this while loop
# o.print()
# print()
# o.pop()
# print()
# o.print()





# class Queue:
#     def __init__(self,capacity):
#         self.capacity=capacity
#         self.q=[None]*capacity
#         self.front=0
#         self.rear=-1
#         self.size=0
#     def enque(self,data):
#         if self.size==self.capacity:
#             print("queue is full")
#         self.rear+=1
#         self.q[self.rear]=data
#         self.size+=1
#     def deque(self):
#         if self.size==0:
#             print("queue is empty")
#         deleted=self.q[self.front]
#         self.front+=1
#         self.size-=1
#         print("dequeued ele is",deleted)
#     def is_empty(self):
#         if self.size==0:
#             print("True")
#         else:
#             print("False")
#     def peek(self):
#         if self.size==0:
#             print("queue is empty" )
#         print(self.q[self.front])
#     def print(self):
#         i=self.front
#         e=self.rear
#         while i<=e:
#             print(self.q[i],end=" ")
#             i+=1
# capacity=int(input())
# o=Queue(capacity)
# while True:
#     a=int(input())
#     if a==0:
#         break
#     o.enque(a)
# o.print()
# print()
# o.deque()
# print()
# o.peek()
# print()
# o.is_empty()
# print()
# o.print()
