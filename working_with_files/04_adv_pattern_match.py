import os, fnmatch

def match(fld, search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)

match ('./working_with_files/work_files', '*_file*.*')