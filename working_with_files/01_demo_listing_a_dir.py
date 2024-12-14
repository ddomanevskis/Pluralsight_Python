import os

def list_dir(fld):
    for fn in os.listdir(fld):
        print(fn)

list_dir('./working_with_files/work_files')