# s='yaswanth'
# #slicing
# """jdgurjfg"""
# print(s[1:6:2])
# print(s[::-1])
# print(s[:5:])
# print(s[1::-1])
# print(dir(dict))

s='ALL Python string methods'
print(s.count('a'))
print(s.find('y'))#if not found returns -1
print(s.rfind(s))#finds from indexing right to left
print(s.index('i'))
print(s.rindex('s'))
print(s.startswith('y'))
print(s.endswith('s'))
print(s.upper())
print(s.lower())
print(s.capitalize())#only char at index 0
print(s.title())#first letter of each word 
print(s.swapcase())#lower to upper vice versa
print(s.casefold())#aggresive lowercase used for comparisions
print(s.strip())#removes extra spaces from left and right not inbetween
print(s.lstrip())
print(s.rstrip())
print(s.replace('y','z'))
print(s.split(' ',1))#splits into list of strings
print(s.rsplit(' ',1))#differ when we split like limit
print(s.splitlines())
print('-'.join(s))# adds given sign in b/w the string
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.isupper())
print(s.islower())
print(s.isspace())
print(s.istitle())
print(s.isidentifier())
print(s.isnumeric())
print(s.isdecimal())
print(s.isprintable())
print(s.center(100))
print(s.ljust(100))
print(s.rjust(100))
print(s.zfill(100))#fills with 0 from left
a=s.encode('utf-8')
print(a)
print(a.decode('utf-8'))
import string
print("hi, yash!".translate(str.maketrans("", "", string.punctuation)))#removing
print("hello world".translate(str.maketrans("", "", "aeiou")))# deleting 
print("{} scored {} marks".format("yash", 95))
print("{name} scored {marks} marks".format_map({"name": "yash", "marks": 95}))
print("a\tb".expandtabs(0))
print(s.partition('n'))
print(s.rpartition('t'))
print(s.removeprefix('ALL'))#removes the prefix and gives remaining
print(s.removesuffix('methods'))