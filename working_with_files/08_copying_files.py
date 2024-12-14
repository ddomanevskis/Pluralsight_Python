import shutil

def copy_file(src, dst):
    shutil.copy(src, dst)

def copy_folder(src, dst):
    shutil.copytree(src, dst)

copy_file('./working_with_files/work_files/names.csv', './working_with_files/work_files/names_copy.csv')
copy_folder('./working_with_files/work_files', './working_with_files/work_files_copy')