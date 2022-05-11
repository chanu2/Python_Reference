# 시간 복잡도    Python은 일반적으로 1초에 2000만의 연산이 가능
#시간제한이 1초인 문제를 풀때
# N의 범위가 500인 경우 시간복잡도 O(N**3)
# N의 범위가 2000인 경우 시간복잡도 O(N**2)
# N의 범위가 100000인 경우 시간복잡도 O(NlogN)
# N의 범위가 10000000인 경우 시간복잡도 O(N)


#리스트 컨프리헨션
# A=[i for i in range(10)] = [0,1,2,3,4,5,6,7,8,9]
# A=[i for i in range(10) if i%2==1] = [1,3,5,7,9]  
# 2차원 리스트 초기화   n=4,m=3   A=[[0]*m for _  in range(n)]   4행 3열의 2차원 리스트

#리스트에서 특정 값을 가지는 원소 모두 제거
# a=[1,2,3,3,4,5,5,5]
# remove_set={3,5}   # 집합자료형
# result=[ifor i in a if i not in remove_set]

#튜플


# 딕션어리 
# 딕션어리 선언시 간단하게 
# a=[1,2,3,4,5,6,7,8,9,10]  -->   dic={a[i]:i for i in range(10)} 


#집합



#  함수
# def add(a,b):
#     return a+b
# print(add(7,3))     
# print(add(b=3,a=9))


#global
# 전역변수 지역변수

# array=[1,2,3,4,5,6]
# def func():
#     array=[1,2,3,4]
#     array.append(100)
#     print(array)
# func()
# print(array)


#여러 개의 반환값 (패킹, 언패킹)

# def operation(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b                  #패킹
#     div=a/b
#     return add,sub,mul,div
# a,b,c,d=operation(9,3)        #언패킹
# print(a,b,c,d)    


#lambda 표현식
# print((lambda a,b:a+b)(3,7))


# array=[('chan',50),('ha',70),('jun',90)]

# def my_key(x):
#     return x[1]
# print(sorted(array,key=my_key))
# print(sorted(array,key=lambda x:x[1]))    


#COUNTER
# # 등장 횟수를 세는 기능 
# from collections import Counter
# counter=Counter([1,1,1,1,2,2,3,4,4,5,5,5,5,5,5,5,5])
# print(counter[1])                #리스트 안의 요소 세는 기능
# print(counter[4])
# print(dict(counter))

#math 모듈
# 최대공약수, 공배수 모두 가능 gcd,lcm


# 재귀함수 recursive function
# def recursive_function(i):
#     if i==100:
#         return
#     print(i,"번째 재귀함수에서",i+1,"번째 재귀함수를 호출합니다")
#     recursive_function(i+1)
#     print(i,"번째 재귀함수를 종류합니다")

# recursive_function(40)




# 재귀함수 예시 fectorial
# def fectorial(n):
#     if n<=1:
#         return 1
#     return n*fectorial(n-1)
# print(fectorial(5))        


# 재귀함수 예시 최대공약수(뉴클리드 호제법)
# 두 자연수 a,b에 대하여 (a>b) a를 b로 나눈 나머지를 r이라고 하면
# 이때 a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# def gcd(a,b):
#     if a%b==0:
#         return b
#     else:
#         return gcd(b,a%b)    






#DFS(Depth-First-Search) 깊이 우선 탐색
#끝까지 다 탐색하는거--> stack or 재귀함수  재귀함수를 사용하면 backtracking에 유리하다.

# graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[6,8],[1,7]]
# visited=[False]*9

# def dfs(graph,v,visited):
#     visited[v]=True
#     print(v,end=' ')

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)
# print(dfs(graph,1,visited))            
    
          




##BFS 넓이 우선 탐색
# graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[6,8],[1,7]]
# visited=[False]*9
# from collections import deque   
# def bfs(graph,start,visited):

#     queue=deque([start])
#     visited[start]=True

#     while queue:
#         v=queue.popleft()
#         print(v,end=' ')

#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i]=True

# print(bfs(graph,1,visited))      




# 선택 정렬  # n+(n-1)+(n-2)+....2 --> 시간복잡도 n*2
# array=[7,5,9,0,3,1,6,2,4,8]
# for i in range(len(array)):
#     mini=i
#     for j in range(i+1,len(array)):
#         if array[mini]>array[j]:
#             mini=j
#     array[i],array[mini]=array[mini],array[i]

# print(array)



# 삽입정렬 
# 시간복잡도가  n*2   but 이미 다 정렬되어있다면 n으로 시간복잡도는 줄어든다
# array=[7,5,9,0,3,1,6,2,4,8]

# for i in range(1,len(array)):
#     for j in range(i,0,-1):
#         if array[j]<array[j-1]:
#             array[j],array[j-1]=array[j-1],array[j]    
#         else:
#             break    
# print(array)        




##### quick sort !!!!
#시간 복잡도가 빠르다 NlogN  최악의 경우 N*2 까지 나온다.

# array=[5,7,9,0,3,1,6,2,4,8]
# def quick(array,start,end):
#     if start >= end:      # 정렬하려는 원소가 1개 일때 종료
#         return
#     pivot=start       # 첫번째 기준이 되는 값을 설정
#     left=start+1      # pivot의 바로 오른쪽 인덱스를 left로 설정 
#     right=end         # 가장 오른쪽 값을 rigjt로 설정
#     while left <= right:          # 겹쳐지지 않을 때 까지 반복 
#         while left <=end and array[left]<=array[pivot]:      # left에서 부터 pivot보다 큰 수를 찾고 
#             left+=1
#         while right > start and array[right]>=array[pivot]:     # right 부터 pivot보다 작은 수를 찾고
#             right-=1
#         if left > right:     # 겹쳐질때  
#             array[right],array[pivot]=array[pivot],array[right]   # pivot 값과 rigjt값을 서로 바꾼다.
#         else:
#             array[right],array[left]=array[left],array[right]   # left 값과 right 값을 서로 바꿔준다.
#         quick(array,start,right-1)          # pivot을 기준으로 왼쪽 부분과 오른쪽 부분을 따로 따로 다시 QUICK SOLT 해준다.
#         quick(array,right+1,end)
# quick(array,0,len(array)-1)
# print(array)      




####3 퀵정렬 파이썬으로 간단하게  --> 리스트 슬라이싱, 컴프리헨션

# array=[5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array):
#     if len(array)<=1:     #리스트가 하나의 원소만 가지고 있다면 종료 
#         return array   
#     pivot=array[0]        # pivot값을 리스트의 첫번째 값으로 설정
#     tail=array[1:]        # pivot값을 제외한 나머지를 리스트 슬라이싱

#     left_side=[x for x in tail if x <=pivot]     #pivot 기준 작은 수들을 왼쪽으로 정렬
#     right_side=[x for x in tail if x > pivot]    #pivot 기준 큰 수들을 오른쪽으로 정렬

#     return   quick_sort(left_side)+[pivot]+quick_sort(right_side)   # 재귀를 이용하여  pivot을 제외한 왼쪽과 오른쪽을 각각 따로 정렬한다.

# print(quick_sort(array))      




# 반복문으로 구현한 이진탐색 코드
# import sys
# def binary_search(array,target,start,end):
#     while start<= end:
#         mid = (start+end)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid] > target:
#             end=mid-1
#         else:
#             start=mid+1
#     return None

# n,target =list(map(int,sys.stdin.readline().split())) 
# array=list(map(int,sys.stdin.readline().split())) 
# result =binary_search(array,target,0,n-1)
# if result ==None:
#     print("원소가 없다")
# else:
#     print(result+1)     





#계수 정렬 
# 특정 조건이 부합할때만 매우 빠르게 동작하는 알고리즘 최악의 경우/// 데이터 개수가 N,데이터(양수) 중 최대값 K O(K+K)
# 데이터의 크기 범위가 제한되어 정수 형태로 표현 할 수 있을때 사용가능

# array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]   # 모든 원소의 값이 0보다 크다고 가정

# count=[0]*(max(array)+1)     # 모든 범위를 포함하는 리스트 선언(모두 0 으로 초기화)

# for i in range(len(array)):  # 각 데이터에 해당하는 인덱스 값 증가
#     count[array[i]]+=1

# for j in range(len(count)):
#     for k in range(count[k]): # count 값을 확인 후 출력
#         print(k,end=' ')





## 이진탐색 알고리즘 
# 순차 탐색 --> 리스트에서 특정한 데이터를 찾기위해 앞에서 부터 데이터를 하나씩 확인하는 방법
# 이진 탐색 --> #정렬 되있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법  logN 보장
# 이진 탐색(시작점,중간점,끝 인덱스필요)


# 재귀함수를 이용한 이진탐색 코드
# import sys
# def binary_search(array,target,start,end):    # 리스트,찾을 값, 시작점, 끝 점
#     if start > end:               # None 리턴 조건
#         return None
#     mid=(end+start)//2           #중간값의 인덱스를 구하는 코드
#     if array[mid]==target:       # 중간값이 찾는 값일 떄 인덱스를 반환
#         return mid                
#     elif array[mid]>target:      # 중간값이 찾는 값 보다 클 때 중간값 인덱스 -1 이후로는 볼 필요가 없다
#         return binary_search(array,target,start,mid-1)    
#     else:
#         return binary_search(array,target,mid+1,end) #중간값이 찾는 값 보다 작을 때 중간값 인덱스 +1 이 전으로는 볼 필요가 없다.

# n,target=map(int,sys.stdin.readline().split())
# array=list(map(int,sys.stdin.readline().split()))  

# result=binary_search(array,target,0,n-1)
# if result==None:     #원소가 존재하지 않을 때
#     print("원소가 없다")
# else:
#     print(result+1)




# # 반복문으로 구현한 이진탐색 코드
# import sys
# def binary_search(array,target,start,end):
#     while start<= end:
#         mid = (start+end)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid] > target:
#             end=mid-1
#         else:
#             start=mid+1
#     return None

# n,target =list(map(int,sys.stdin.readline().split())) 
# array=list(map(int,sys.stdin.readline().split())) 
# result =binary_search(array,target,0,n-1)
# if result ==None:
#     print("원소가 없다")
# else:
#     print(result+1)                      




# 파이썬 이진 탐색 라이브러리
# bisect_left(a,x) --> 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a,x) --> 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

# 값이 특정 범위에 속하는 데이터 개수 구하기
# from bisect import bisect_left,bisect_right
# def cuont_range(a,left_vlaue,right_vlaue):
#     return  bisect_right(a,right_vlaue)-bisect_left(a,left_vlaue)

# a=[1,2,3,3,3,3,4,4,8,9]
# print(cuont_range(a,4,4))




## 파라메트릭 서치## 이진탐색 문제 활용은 파라메트릭 서치가 많이 나온다
#최적화 문제(어떠한 함수의 값을 가능한 낮추거나 함수의 값을 높이는 문제들을 의미한다)를 결정 문제('예',혹은 '아니오')로 바꾸어 해결하는 기법


# 떡볶이 문제 
# import sys
# n,m=map(int,sys.stdin.readline().split())
# array=list(map(int,sys.stdin.readline().split()))

# start=0
# end=max(array)
# result=0

# while start<=end:
#     total=0
#     mid=(end+start//2)
#     for i in array:
#         if i>mid:
#             total+=i-mid
#     if total>=m:
#         start=mid+1
#         result=mid
#     else:
#         end=mid-1
# print(result)


# 요소개수 확인하기 이진탐색으로 nlogn
# import sys
# from bisect import bisect_left,bisect_right
# n,m=map(int,sys.stdin.readline().split())
# array=list(map(int,sys.stdin.readline().split()))

# def count_component(array,m):
#     result=bisect_right(array,m)-bisect_left(array,m)
#     if result==0:
#         return -1
#     else:
#         return result    
# print(count_component(array,m))
