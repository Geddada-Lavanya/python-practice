#Trie,heap,monotonic stack


#WORD SEARCH-2
# it can do by using trie
#here are we are doing backtracking also

#Trie DataStructure

    # class trie_node:
    #     def __init__(self):
    #         self.child={}
    #         self.is_end=False

    #     def add_word(self,word): # self is root object
    #         curr=self
    #         for w in word:
    #             if w not in curr.child:
    #                 curr.child[w]=trie_node()
    #             curr=curr.child[w]
    #         curr.is_end=True

    # class Solution:
    #     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #         root=trie_node()
    #         for w in words:
    #             root.add_word(w) # root is self in add_word() function

    #         row,col=len(board),len(board[0])
    #         visited,res=set(),set()
    #         def backtrack(r,c,path,root):
    #             if r<0 or c<0 or c==col or r==row or (r,c) in visited or board[r][c] not in root.child :
    #                 return 
    #             visited.add((r,c))
    #             root=root.child[board[r][c]]
    #             path+=board[r][c]
    #             if root.is_end:
    #                 res.add(path)
    #             backtrack(r-1,c,path,root)
    #             backtrack(r,c-1,path,root)
    #             backtrack(r+1,c,path,root)
    #             backtrack(r,c+1,path,root)
    #             visited.remove((r,c))

    #         for r in range(row):
    #             for c in range(col):
    #                 backtrack(r,c,"",root)
    #         return list(res)


#heafipy min heap
    # import heapq
    # arr=[2,6,4,8,9,12,3]
    # heapq.heapify(arr)
    # print(arr) #min heap
    # print(arr[0])
    # heapq.heappop(arr)
    # print(arr)
    # heapq.heappush(arr,1)
    # print(arr)


#heafipy max heap
    # import heapq
    # arr=[-2,-6,-4,-8,-9,-12,-3]
    # heapq.heapify(arr)
    # print(arr) #max heap
    # print(arr[0])
    # heapq.heappop(arr)
    # print(arr)
    # heapq.heappush(arr,-1)
    # res=[-i for i in arr]
    # print(res)


#print kth largest element
    # import heapq
    # arr=[2,6,4,8,9,12,3]
    # k=2
    # res=[]
    # for num in arr:
    #     heapq.heappush(res,num)
    #     if len(res)>k:
    #         heapq.heappop(res)
    # print(res[0])


#next greater element-1
    # nums1=[4,1,2]
    # nums2=[1,3,4,2]
    # hash_map={}
    # res=[-1]*len(nums1)
    # stack=[]
    # for i in range(len(nums1)):
    #     hash_map[nums1[i]]= i
    # for j in range(len(nums2)):
    #     while stack and stack[-1]<nums2[j]:
    #         temp=stack.pop()
    #         res[hash_map[temp]]=nums2[j]
    #     if nums2[j] in hash_map:
    #         stack.append(nums2[j])
    # print(res)