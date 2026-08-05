n=1
def solve(n):
    if n>10:
     return 
    print(n,end=" ")
    return solve(n+1)
solve(n)




def fun(n):
   if n:
      print(n,end="")
      fun(n-1)
      print(n,end=" ")
fun(4)



#permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(nums,path):
            if len(nums)==0:
                res.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],path+[nums[i]])
        backtrack(nums,[])
        return res


#Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, s: str) -> List[str]:
        res=[]
        hash_map={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        "23"
        def backtrack(i,path):
            if i==len(s):
                res.append(path)
                return
            for v in hash_map[s[i]]:
                backtrack(i+1,path+v)
        backtrack(0,"")
        return res
    
    

#N-Queen
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[["."]*n for _ in range(n)]
        def is_safe(row,col):
            #upper
            for r in range(row):
                if board[r][col]=="Q":
                    return False
            # left diagonal
            r,c=row-1,col-1
            while r>=0 and c>=0:
                if board[r][c]=="Q":
                    return False
                r-=1
                c-=1
            # right diagonal
            r,c=row-1,col+1
            while r>=0 and c<n:
                if board[r][c]=="Q":
                    return False
                r-=1
                c+=1
            
            return True

        def backtrack(row):
            if row==n:
                res.append(["".join(row) for row in board])
                return
            for col in board:
                if is_safe(row,col):
                    board[row][col]="Q"
                    backtrack(row+1)
                    board[row][col]="."
        backtrack(0)
        return res



#word search-1
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row,col=len(board),len(board[0])
        visited=set()
        def backtrack(r,c,i):
            if i==len(word):
                return True
                
            if r<0 or c<0 or r==row or c == col or (r,c) in visited or word[i]!=board[r][c]:
                return False

            visited.add((r,c))
            res=backtrack(r-1,c,i+1) or backtrack(r,c-1,i+1) or backtrack(r+1,c,i+1) or backtrack(r,c+1,i+1)


        for r in range(row):
            for c in range(col):
                if backtrack(r,c,i=0):
                    return True
        return False
