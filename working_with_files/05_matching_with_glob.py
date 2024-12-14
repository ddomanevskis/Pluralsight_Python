from pathlib import Path

def glob_match(fld, search):
    p = Path(fld)
    for n in p.glob(search):
        print(n)

glob_match('./working_with_files/work_files', '*2*.t*')
glob_match('./working_with_files/work_files', '*_file_*.t*')
