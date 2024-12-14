import zipfile


def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extract(fn, path=path)


def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path=path)


extract_file(
    './working_with_files/work_files_copy/files.zip',
    'working_with_files/work_files_copy/example.txt',
    './working_with_files/work_files_copy')
extract_all(
    './working_with_files/work_files_copy/files.zip',
    './working_with_files/extracted')
