import zipfile

to_add = ['./working_with_files/work_files_copy/authors.json',
          './working_with_files/work_files_copy/person.xyz']

def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for f in files:
            lst = archive.namelist()
            if not f in lst:
                archive.write(f)
            else:
                print(f'Error: {f} already in archive')

add_to_zip('./working_with_files/work_files_copy/files.zip', to_add, 'a')