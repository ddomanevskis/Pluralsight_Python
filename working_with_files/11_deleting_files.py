import os

def remove_file(f):
    if os.path.is_file(f):
        try:
            os.remove(f)
        except OSError as e:
            print(f'Error: {f} : {e.strerror}')
    else:
        print(f'Error: {f} : not a file')

remove_file('./working_with_files/work_files_copy/names_renamed.csv')