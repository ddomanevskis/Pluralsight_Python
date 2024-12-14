import os
from pathlib import Path

def rename_file(src, dst):
    os.rename(src, dst)

def rename_file_2(src, dst):
    f = Path(src)
    f.rename(dst)

rename_file('./working_with_files/work_files_copy/names.csv', './working_with_files/work_files_copy/names_renamed.csv')
rename_file_2('./working_with_files/work_files_copy/names_renamed.csv', './working_with_files/work_files_copy/names.csv')