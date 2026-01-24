import random as rand

my_list = ['apple', 'banana', 'cherry', 'mango']
random_item = rand.choice(my_list)
print(random_item)

print(rand.randint(1,100))
li=[rand.randint(1,100) for _ in range(10)]
print(li)

print(rand.random())#gives output b/w 0,1 float

print(rand.uniform(1, 10))#float range gives float value

print(rand.sample(my_list, 2))#no duplicates in selection

print(rand.choices(my_list, k=5))#duplication allowed

rand.shuffle(li)
print(li)

rand.seed(1)#will tells how many time a number can be repeated
print([rand.randint(1,100) for _ in range(10)])
