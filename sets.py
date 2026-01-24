s={}
print(type(s))
# {1, 2, 3}
# {"a", "b"}
# {1, 2.5, "x"}
# {(1, 2), (3, 4)}   # tuple is immutabl
s=set()
print(type(s))
s={1,2,3,4,5,6,7,8,(1,2),(1,2,3)}#dont have index
s.add(10)
print(s)
s.update([20,21])#adds iterable elements not list 
print(s)
s.remove(1)#throws error if not present
s.discard(1)#if element not present dont give error
print(s)
print(s.pop())#returns arbitrary element
s.clear()
del s
s={1}
p=s.copy()
print(p,type(p))
s,p={1,2,3},{2,3,4,5}
print(s|p)#union
print(s-p)#diff
print(s&p)#intersection
print(s^p)#uncommon
print(s.issubset(p))
print(s.issuperset(p))
print(s.isdisjoint(p))
s={x*x for x in range(5)}
print(s)
print(len(s))
print(max(s))
print(min(s))
print(sum(s))
print(sorted(s,reverse=-1))  
 # returns list
print(any(s))
print(all(s))
#important 
f=frozenset([1,2,3,4,5])
print(f)
# Immutable set
# Can be dictionary key

# Can be element of another set
