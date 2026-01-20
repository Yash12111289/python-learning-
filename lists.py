# l=[1,'a',True,3.54]
# a=[]
# b=list()
# print(list('yaswanth'))
# print(l)
# print(list(range(1,10,2)))
# a=[x for x in range(0,5)]
# a=[x for x in range(0,10) if x%2==0]
# print(a)
# a=[int(input()) for _ in range(2)]
# print(a)
# a=list(map(int, input().split()))
# print(a)
# a=input().split()
# print(a)
# r,c=map(int,input().split())
# a=[list(map(int, input().split())) for _ in range(r)]
# print(a)
a=[1,2,3,4,5]
print(len(a))
a.append(6)
print(a[::-1])
a[2]=10
print(a)
print(a+[3,44])
print(a*2)
print(1 in a)
print(11 not in a)
print(a*2==a+a)
print(a<a*2)
a.append(30)
a.extend([1,2])
a.insert(0,0)
a.remove(0)#deletes first occurance
print(a)
print(a.pop())
# print(a.clear())
print(a.index(2))
a.sort()
print(a)
a.sort(reverse=-1)
print(a)
a.reverse()
print(a)
print(a.copy())#creates copied version not like a=b it is referencing one
print(sorted(a))
a=list(enumerate(a,start=1))
a=list(zip(a,['a','b']))
print(a)
a=list(filter(lambda x: x%2== 0, range(20)))
print(a)
from functools import reduce
print(reduce(lambda x,y:x*y,[1,2,3,4]))