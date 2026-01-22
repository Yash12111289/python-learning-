"""
PYTHON FILE SYSTEM – RUNNING NOTES (7 → 20)
------------------------------------------
This script demonstrates:
- Listing files
- Walking directories
- Delete / Rename / Move
- Copy files
- Path handling
- pathlib usage
- Permissions
- Metadata
- Glob search
- Temp files
- Exception handling
- Binary files
- Best practices
- Real-world examples
"""

import os
import shutil
import glob
import tempfile
from pathlib import Path
import stat

# ===============================
# 7️⃣ LIST FILES IN DIRECTORY
# ===============================

print("Listing current directory:")
print(os.listdir("."))  # lists files & folders

# Recursive directory walk
print("\nWalking directory tree:")
for root, dirs, files in os.walk("."):
    print("ROOT:", root)
    print("FILES:", files)
    break  # break to avoid huge output

# ===============================
# 8️⃣ DELETE / RENAME / MOVE FILE
# ===============================

# create a sample file
with open("sample.txt", "w") as f:
    f.write("Hello File System")

# rename file
os.rename("sample.txt", "renamed.txt")

# move file
shutil.move("renamed.txt", "moved.txt")

# delete file
os.remove("moved.txt")

# ===============================
# 9️⃣ COPY FILES & DIRECTORIES
# ===============================

with open("a.txt", "w") as f:
    f.write("Copy me")

shutil.copy("a.txt", "b.txt")  # file copy

os.mkdir("src")
with open("src/x.txt", "w") as f:
    f.write("inside folder")

shutil.copytree("src", "dest")  # folder copy

# ===============================
# 🔟 PATH HANDLING (os.path)
# ===============================

path = os.path.join("folder", "file.txt")  # OS independent path
print("\nJoined path:", path)
print("Base name:", os.path.basename(path))
print("Dir name:", os.path.dirname(path))
print("Absolute:", os.path.abspath(path))

# ===============================
# 1️⃣1️⃣ pathlib (MODERN WAY)
# ===============================

p = Path("note.txt")
p.write_text("Using pathlib")
print("\nPathlib read:", p.read_text())

# create nested dirs
Path("a/b/c").mkdir(parents=True, exist_ok=True)

# iterate files
print("Iterating current dir using pathlib:")
for file in Path(".").iterdir():
    print(file)

# ===============================
# 1️⃣2️⃣ FILE PERMISSIONS
# ===============================

# chmod (read/write/execute)
os.chmod("note.txt", 0o644)  # rw-r--r--

# ===============================
# 1️⃣3️⃣ FILE METADATA
# ===============================

info = os.stat("note.txt")
print("\nFile size:", info.st_size)
print("Last modified:", info.st_mtime)

# ===============================
# 1️⃣4️⃣ SEARCH FILES (glob)
# ===============================

print("\nText files:", glob.glob("*.txt"))
print("Recursive python files:", glob.glob("**/*.py", recursive=True))

# ===============================
# 1️⃣5️⃣ TEMPORARY FILES
# ===============================

with tempfile.NamedTemporaryFile(delete=False) as tmp:
    tmp.write(b"Temporary data")
    print("\nTemp file created:", tmp.name)

# ===============================
# 1️⃣6️⃣ EXCEPTION HANDLING
# ===============================

try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Handled: File not found")
except PermissionError:
    print("Handled: Permission denied")

# ===============================
# 1️⃣7️⃣ BINARY FILE HANDLING
# ===============================

with open("binary.bin", "wb") as f:
    f.write(b"\x00\x01\x02")

with open("binary.bin", "rb") as f:
    print("Binary content:", f.read())

# ===============================
# 1️⃣8️⃣ BEST PRACTICES (SHOWN)
# ===============================
# ✔ with open()
# ✔ pathlib
# ✔ exception handling
# ✔ no hard-coded separators

# ===============================
# 1️⃣9️⃣ REAL-WORLD EXAMPLES
# ===============================

# count lines in file
with open("a.txt") as f:
    line_count = sum(1 for _ in f)
print("\nLine count in a.txt:", line_count)

# copy only .txt files to backup
Path("backup").mkdir(exist_ok=True)
for file in Path(".").glob("*.txt"):
    shutil.copy(file, "backup")

# ===============================
# 2️⃣0️⃣ INTERVIEW SUMMARY (CODED)
# ===============================

summary = {
    "read/write": "open()",
    "paths": "pathlib",
    "copy/move": "shutil",
    "search": "glob",
    "metadata": "os.stat",
    "temp": "tempfile"
}

print("\nInterview summary:", summary)

print("\n--- END OF FILE SYSTEM NOTES ---")
