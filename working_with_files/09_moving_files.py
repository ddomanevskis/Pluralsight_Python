import shutil

def mv_files(src, dst):
    shutil.move(src, dst)

mv_files('./working_with_files/work_files/names.csv', './working_with_files/work_files_copy/names_moved.csv')