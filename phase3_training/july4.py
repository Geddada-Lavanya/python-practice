# Dyanamic Programming

#fibonacci using recursion
    # def fibonacci(n):
    #     if n<2:
    #         return n
    #     return fibonacci(n-1)+fibonacci(n-2)
    # print(fibonacci(7))


#check how many time the function run
    # count=0
    # def fibonacci(n):
    #     global count
    #     count+=1
    #     if n<2:
    #         return n
    #     return fibonacci(n-1)+fibonacci(n-2)
    # res=fibonacci(40)
    # print(count,res)  # output takes so much of time this TLE Error


#Memoization
    # def fibonacci(n,memo):
    #     if n<2:
    #         return n
    #     if memo[n]!=-1:
    #         return memo[n]
    #     memo[n]= fibonacci(n-1,memo)+fibonacci(n-2,memo)
    #     return memo[n]
    # n=7
    # memo=[-1]*(n+1)
    # res=fibonacci(n,memo)
    # print(res)


#check memoization how many times the fun run
    # def fibonacci(n,memo):
    #     global cnt
    #     cnt+=1
    #     if n<2:
    #         return n
    #     if memo[n]!=-1:
    #         return memo[n]
    #     memo[n]= fibonacci(n-1,memo)+fibonacci(n-2,memo)
    #     return memo[n]
    # n=100
    # cnt=0
    # memo=[-1]*(n+1)
    # res=fibonacci(n,memo)
    # print(res)
    # print(cnt) # it takes less time to run for larger inputs


#Tabulation
    # def fib(n):
    #     dp=[0]*(n+1)
    #     dp[1]=1
    #     for i in range(2,n+1):
    #         dp[i]=dp[i-1]+dp[i-2]
    #     return dp[n]
    # res=fib(10)
    # print(res)


# Space Optimization 
    # def fib(n):
    #     f1,f2=0,1
    #     for _ in range(n-1):
    #         res=f1+f2
    #         f1=f2
    #         f2=res
    #     return res
    # print(fib(7))



# Coin change(Tabulation)
    # class Solution:
    #     def coinChange(self, coins: List[int], amount: int) -> int:
    #         dp=[float('inf')]*(amount+1)
    #         dp[0]=0
    #         for amt in range(1,amount+1):
    #             for c in coins:
    #                 if amt-c>=0:
    #                     dp[amt]=min(dp[amt],dp[amt-c]+1)
    #         return -1 if dp[amount]==float('inf') else dp[amount]



# House Robber


