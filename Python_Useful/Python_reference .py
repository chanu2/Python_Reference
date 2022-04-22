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
