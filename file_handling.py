# Module	  Purpose
# os	      Low-level OS & file system ops
# os.path	  Path manipulation
# pathlib	  Modern, object-oriented paths ✅
# shutil	  High-level file operations
# glob	      Pattern-based file search
# tempfile	  Temporary files
# stat	      File permissions & metadata


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

    
import os
print(os.getcwd())#current working directory(cwd)-file path

print(os.path.exists("file.txt"))
print(os.path.isfile("file.txt"))
print(os.path.isdir(r"C:\Users\yaswa\Downloads\python"))#here 'r' will helps as excape sequence like if any type of string error occurs
print(os.path.getsize("file.txt"))
print(os.path.abspath("file.txt"))

os.mkdir("dir1")
os.makedirs("a/b/c", exist_ok=True)

import shutil
os.rmdir("dir1")           # empty only
shutil.rmtree("a")         # force delete

os.listdir(".")


