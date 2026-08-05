
# def adjecency_matrix(vertex_data,matrix,n):
#     connected=[]
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j]==1:
#                 connected.append(vertex_data[j])
#         print(f"{vertex_data[i]}: is connected to {connected}")
#         connected=[]

# n=int(input())
# vertex_data=[None]*n
# for i in range(n):
#     vertex_data[i]=input()
# matrix=[]
# for i in range(n):
#     sb=[]
#     print(f"enter data for row {i+1}")
#     for j in range(n):
#         sb.append(int(input()))
#     matrix.append(sb)
# adjecency_matrix(vertex_data,matrix,n)


# def level_order(self,root):
#         if not root:
#             return
#         self.q.append(root)
#         while len(self.q)!=0:
#             temp=self.q.pop(0)
#             print(temp.data,end=" ")
#             if temp.left:
#                 self.q.append(temp.left)
#             if temp.right:
#                 self.q.append(temp.right)




# def dfs(graph,node,visited=None):
#     if visited is None:
#         visited=set()
#     visited.add(node)
#     print(node,end=" ")
#     for neighbour in graph:
#         if neighbour is not visited:
#             dfs(graph,neighbour,visited)
# graph={'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':[],'F':[]}
# dfs(graph,'A')



# def linear_search(arr,target):
#     n=len(arr)
#     for i in range(n):
#         if arr[i]==target:
#             print(i)
#             break              #return 
#     print(-1)
# arr=list(map(int,input().split()))
# target=int(input())
# linear_search(arr,target)


# def binary_search(arr,tar):
#     l,r=0,len(arr)-1
#     while l<=r:
#         mid=(l+r)//2
#         if arr[mid]==tar:
#             return mid
#         elif arr[mid]>tar:
#             r=mid-1
#         else:
#             l=mid+1
#     return -1
# arr=list(map(int,input().split()))
# tar=int(input())
# print(binary_search(arr,tar))
    

