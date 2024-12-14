import os

def ends_with(fld, search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)

def starts_with(fld, search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)

ends_with('./working_with_files/work_files', '.txt')
starts_with('./working_with_files/work_files', 'names')