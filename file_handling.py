

f=open("file.txt",'w')
f.write('hello')
f.close()

#instead of it use open for auto close file 
with open('file.txt','a') as f:#->r,w,a,x 
    f.write(' world')
'''by default access modifier will be read only 
   we can change accordingly 
   w-write to exiting overwriting it
   a-adds text at end append
   x-creates file if not exists throws error if present
'''
with open('file.txt','r+') as f:
    f.read()
    f.write(' thank you\n hi')
    '''here output will be 
       hello world thank you
       hi 
       we get confused because we assume output as:
       hello world 
       here we assume after read we used write right it will read upto exiting one no it will read till the end of file'''
with open('file.txt','r+') as f:
    for line in f:
        print(line.strip())
    print(f.tell())#current position of pointer
    f.seek(0)#points to the starting
    lines=f.readlines()#convert lines to lists
    print(lines)
#reading
f=open('file.txt','r+')
print(f.read())
f.seek(0)
print(f.read(10))
f.seek(0)
print(f.readline())
f.seek(0)
print(f.readlines())
# writing
f.seek(0)
f.write('hello yash')#deletes the exiting
li=['hi ','how ','are ','you']
f.writelines(li)
f.seek(0)
print(f.read())
f.seek(0)
#append
f=open('file.txt','a')
f.write('codegnan')
print(f.name,f.mode,f.closed)
f.close()
