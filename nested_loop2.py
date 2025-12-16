# Nested Loop Pair Discovery: Comparing Elements Across Two Arrays
def solution(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            if i < j:
                result.append((i, j))
    return result
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
print(solution(list1,list2))