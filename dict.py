d1 = {}# empty dict
d2 = {"a": 1, "b": 2}#dictionaries keys should be unique and immutable, values can
d3 = dict(a=1, b=2)
d4 = dict([("x", 10), ("y", 20)])
d = dict.fromkeys(["a", "b", "c"], 0)
# {'a': 0, 'b': 0, 'c': 0}
d = dict.fromkeys(["a","b"], [])

print(d["a"],d.get("c"),d.get("x", 0)) # KeyError if missing # None if missing # default value
d.update({"x": 9, "y": 10})
print(d.pop("a"),d.pop("a", 0)) # removes key  # safe remove
print(d.pop("a",0))#pop needs key arg to remove also if we use 0 arg for safe remove if not found
print(d.popitem())
del d["x"]

print(d)
d.clear()
print(d)
d={'a':1,'b':2,'c':3,'d':4}
d.setdefault('x', []).append('y')
d.setdefault('x', []).append(['y'])
d.setdefault('x', []).extend(['z','e'])

print(d)
del d
d = {"a": 1, "b": [10, 20]}
import copy

d1=d.copy()
d2=copy.deepcopy(d)
d['b'].append('30')#shallow copy like creates reference copy but deepcopy will generate new dict completely
# we can see how they are updating the values
#occured mainly in nested dict like containing lists etc
print(d1,d2)
del d
d={x:x*x for x in range(1,6)}
print(d)
#finding
print("a" in d)
print("a" not in d)# by default it checks with in keys if we need to check in values try this
print(1 in d.values())
print(10 in d.values())

print(d.keys())
print(d.values())#this is called tuple unpacking
print(d.items())#this is view of objects

for item in d.items():
    print(item)#gives tuple 

p=d|d4
print(p)#union of two dicts

print(dict(sorted(d.items())))#sorted by keys
print(dict(sorted(d.items(), key=lambda x: x[1],reverse=1)))#sorted by values
#lambda func is a inplace fuction which is not used for recursive and also it is used to perform mathematical operations

#nested dicts
d = {
    "a": {"x": 1},
    "b": {"y": 2}
}
print(d["a"]["x"])

from collections import defaultdict
d = defaultdict(int)
d["a"] += 1
print(d)

from collections import Counter
c = Counter("aabbc")#most used in DSA for frequency questions

print(c)

freq = {}
for x in [1,2,3,4]:
    freq[x] = freq.get(x, 0) + 1
print(freq)

groups = {}
for x in {1,2,3,4,5}:
    groups.setdefault(x, []).append(x)
print(groups)