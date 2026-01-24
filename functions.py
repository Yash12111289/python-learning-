def greet(name):
    print("Hello", name)
greet("Yaswanth")

def great(name='codegnan'):#default parameter overrides
    print('hello',name)
greet('yash')

def info(name, age):
    print(name, age)
info(age=25, name="Raj")#keyword based arguments
info('raj',25)#positional arguments

def total(*args):
    print(sum(args))#overloaded arguments
total(1,2,3,4,5)

def details(**kwargs):
    print(kwargs)
details(name="Raj", age=20)#key word arguments give dict as output also known as **kwargs


#global variable

x = 10
def change():
    global x#makes function variable as global varaible
    x = 20
change()
print(x)


#lambda functions

x=lambda x: x*x 
print(x(10))
x=list(map(lambda x:int(x)**2,input().split()))
print(x)


#function as argument

def apply(f, x):
    return f(x)
print(apply(lambda x: x+1, 5))


#returning multiple values 

def calc(a, b):
    return a+b, a-b
s, d = calc(5, 2)


#type hint optional used in dsa

def add(a: int, b: int) -> int:
    return a + b
def get_nums() -> list[int]:
    return [1, 2, 3]
def person() -> tuple[str, int]:
    return ("Raj", 25)
def marks() -> dict[str, int]:
    return {"math": 90, "eng": 85}
from typing import Any

def process(data: Any) -> Any:
    return data
from typing import Union

def square(x: Union[int, float]) -> float:
    return x * x
def coords() -> list[tuple[int, int]]:
    return [(1, 2), (3, 4)]

class User:
    pass

def get_user() -> User:
    return User()





