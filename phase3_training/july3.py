#topological sort
#dijakstras(positive),bellman ford(negative) ---- both require weights

#Course Schedhule(topological+dfs)

    # class Solution:
    #     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    #         adj=[[] for _ in range(numCourses)]
    #         for u,v in prerequisites: #u-index,v=value
    #             adj[u].append(v)

    #         detect_cycle=set()
    #         def dfs(cur):
    #             if cur in detect_cycle:
    #                 return False
    #             if adj[cur]==[]:
    #                 return True
    #             detect_cycle.add(cur)
    #             for c in adj[cur]:
    #                 if dfs(c)==False:
    #                     return False
    #             adj[cur]=[]
    #             detect_cycle.remove(cur)
    #             return True

    #         for course in range(numCourses):
    #             if dfs(course)==False:
    #                 return False
    #         return True
    

        
#Course Schedhule-2(topological+bfs)
    # class Solution:
    #     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #         adj=[[] for _ in range(numCourses)]
    #         Courses_count=[0]*numCourses
    #         for u,v in prerequisites:
    #             adj[v].append(u)
    #             Courses_count[u]+=1

    #         queue=[] # also use dequeue instead of queue, dequeue takes less tc than queue
    #         for i in range(numCourses):
    #             if Courses_count[i]==0:
    #                 queue.append(i)
    #         res=[]
    #         while queue:
    #             cur=queue.pop(0)
    #             res.append(cur)
    #             if adj[cur] ==[]:
    #                 continue
    #             for nei in adj[cur]:
    #                 Courses_count[nei]-=1
    #                 if Courses_count[nei]==0:
    #                     queue.append(nei)
    #         return res if len(res)==numCourses else []


#Dijkstra

    # import heapq
    # class Solution:
    #     # Returns shortest distances from src to all other vertices
    #     def dijkstra(self, V, edges, src):
    #         # code here
    #         adj=[[] for _ in range(V)]
    #         INF=10**6
    #         for u,v,w in edges:
    #             adj[u].append((v,w))
    #             adj[v].append((u,w))
    #         res=[INF]*V
    #         res[src]=0
    #         pq=[(0,src)] #priority queue
    #         while pq:
    #             d,curr=heapq.heappop(pq)
    #             if d>res[curr]:
    #                 continue
    #             for nei,w in adj[curr]:
    #                 if d+w<res[nei]:
    #                     res[nei]=d+w
    #                     heapq.heappush(pq,(res[nei],nei))
    #         return res 
                
            

#BEllman Ford

    # class Solution:
    #     def bellmanFord(self, V, edges, src):
    #         #code here
    #         INF=10**8
    #         res=[INF]*V
    #         res[src]=0
    #         for i in range(V-1):
    #             # flag=True
    #             for u,v,w in edges:
    #                 if res[u]!=INF and res[u]+w<res[v]:
    #                     res[v]=res[u]+w
    #                     # flag=False
    #             # if flag:
    #             #     return res
            
    #         for u,v,w in edges:
    #                 if res[u]!=INF and res[u]+w<res[v]:
    #                     return [-1]
    #         return res
                



#  Network Delay Time

    # import heapq
    # class Solution(object):
    #     def networkDelayTime(self, times, n, k):
    #         """
    #         :type times: List[List[int]]
    #         :type n: int
    #         :type k: int
    #         :rtype: int
    #         """

    #         # Build adjacency list
    #         adj = {i: [] for i in range(1, n + 1)}
    #         for u, v, w in times:
    #             adj[u].append((v, w))

    #         visited = set()

    #         # (time, node)
    #         pq = [(0, k)]

    #         t = 0

    #         while pq:
    #             cur_w, cur_v = heapq.heappop(pq)   # Correct order

    #             if cur_v in visited:
    #                 continue

    #             visited.add(cur_v)

    #             # Maximum time taken to reach any node
    #             t = max(t, cur_w)

    #             for nei_v, nei_w in adj[cur_v]:
    #                 if nei_v not in visited:
    #                     heapq.heappush(pq, (cur_w + nei_w, nei_v))

    #         return t if len(visited) == n else -1





# Cheapest Flights Within K Stops
    # class Solution:
    #     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    #         distance=[float('inf')]*n
    #         distance[src]=0
    #         for i in range(k+1):
    #             temp=distance.copy()
    #             for u,v,w in flights:#start from 1 node not from source node 
    #                 if distance[u]==float('inf'):# skip inf nodes 
    #                     continue
    #                 if distance[u]+w<temp[v]:
    #                     temp[v]=distance[u]+w
    #             distance=temp.copy()
    #         return distance[dst] if distance[dst]!=float('inf') else -1

