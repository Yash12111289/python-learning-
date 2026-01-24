import os
print(os.getcwd())
print(os.chdir(r'C:\Users\yaswa\Downloads'))
print(os.getcwd())
print(os.listdir())#list of dirctories
os.mkdir('hello')
os.rmdir('hello')
os.chdir(r'C:\Users\yaswa\Downloads\python')
# os.remove('file.txt')
# os.rename('old.txt','new.txt')

#file path

# os.path.join('downloads','file.txt')
print(os.path.exists(r'C:\Users\yaswa\Downloads\python\file_handling.py'))
print(os.path.isfile(r'C:\Users\yaswa\Downloads\python\file_handling.py'))
print(os.path.isdir(r'C:\Users\yaswa\Downloads\python\file_handling.py'))
print(os.path.getsize(r'C:\Users\yaswa\Downloads\python\file_handling.py'))


#biary file

# with open('image.jpg','rb') as f:
#     print(f.read())


#copy file manual

with open('file.txt','r+') as f1, open('file2.txt','r+') as f2:
    f2.write(f1.read())
    f2.seek(0)
    print(f2.read())

#loop in file

with open("file.txt") as f:
    for line in f:
        print(line)#print like each line in new line


'''-------------------------------------------------------------------------'''
#modern path handling

from pathlib import Path
p = Path("file.txt")
print(p.exists())
print(p.is_file())
print(p.read_text())
p.write_text("Hello")


#file encoding

open("file.txt", "r", encoding="utf-8")
print()

#buffering and flushing
f=open('file.txt','r+')
f.write("Hello")
f.flush()  # force write to disk  Used in logging, real-time apps.
f.close()


#working with large file

with open("file.txt") as f:
    for line in f:
        print(line.strip())

#temp files

import tempfile
with tempfile.TemporaryFile(mode="w+") as f:
    f.write("test")
    f.seek(0)
    print(f.read())#Used in testing & secure operations.

#file permissions

import os

os.chmod("data.txt", 0o644)#used in linus

#high level file ops

import shutil

shutil.copy("a.txt", "b.txt")
shutil.move("a.txt", "folder/a.txt")#better than manual copying 
shutil.rmtree("folder")

#meory mapped files 

import mmap

with open("data.txt", "r+") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(mm.readline())# fast access


#file locking
import fcntl

fcntl.flock(f, fcntl.LOCK_EX)#important in databases and logs

#different files

import json
with open('file.json','r+') as f:
    print(json.load(f))
