#
# -- gen_include.py - generate gle-library.gle include  file from all files in include folder
#
import os
import platform
from enum import Enum
import pathlib
import glob
from datetime import datetime
import yaml


include_filename = "gle-library.gle"
include_folder   = "../include"
glob_pattern        = '*.gle'

class OS(Enum):
    WINDOWS = 1
    MACOS = 2
    LINUX = 3

this_os = OS.LINUX
os_type = platform.system()
if os_type == "Windows":
    this_os = OS.WINDOWS
elif os_type == "Linux":
    this_os = OS.LINUX
elif os_type == "Darwin":
    this_os = OS.MACOS
else:
    print(f"Unknown operating system: {os_type} - assuming Linux")

def enumerate_files(root_dir, pattern):
    files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in glob.glob(os.path.join(dirpath, pattern)):
            files.append(filename)
    return files

#gle_files  = enumerate_files(include_folder, glob_pattern)

cwd = os.getcwd()
os.chdir(include_folder)
gle_files = []
for filename in glob.glob(glob_pattern):
    gle_files.append(filename)

with open( include_filename, "w") as f:
    f.write(f"!\n")
    f.write(f"! -- {include_filename} -- Global include filename for all routines in the GLE library\n")
    f.write(f"!\n")
    f.write(f"!    Automatically generated by scripts/gen_include.py\n")
    f.write(f"!\n")
    for file in gle_files:
        if(file != include_filename):
            f.write(f"include \"{file}\"\n")

os.chdir(cwd)
print(f"{include_filename} generated successfully")
