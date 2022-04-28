#example 1: Using as module
from importlib.resources import path
import os

#file name with extension
file_name= os.path.basename('/root/file.ext')

#file name without extension
print(os.path.splitext(file_name) [0])

#Example 2: using path module
from pathlib import Path

print(Path('/root/file.ext').stem)