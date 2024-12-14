import os

def traverse(fld):
    for fldpath, dirs, fls in os.walk(fld):
        print(f'Folder: {fldpath}')
        for fn in fls:
            print(f'\t{fn}')

traverse('./working_with_files/work_files')