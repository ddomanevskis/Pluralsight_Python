import zipfile

to_zip = ['./working_with_files/work_files_copy/names.csv', 
          './working_with_files/work_files_copy/names_copy.csv', 
          './working_with_files/work_files_copy/example.txt']

def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for f in files:
            archive.write(f)

create_zip('./working_with_files/work_files_copy/files.zip', to_zip, 'w')