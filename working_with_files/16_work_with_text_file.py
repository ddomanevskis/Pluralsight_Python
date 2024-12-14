def read_txt(fn):
    with open(fn) as f:
        print(f.read())

def read_txt_by_line(fn):
    with open(fn) as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
            line = f.readline()

def write_new_txt(fn, str):
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(str)

def append_line_txt(fn, str):
    with open(fn, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(str)

read_txt('./working_with_files/work_files_copy/example.txt')
read_txt_by_line('./working_with_files/work_files_copy/example.txt')
write_new_txt('./working_with_files/work_files_copy/example.txt', 'this is one more test to test')
append_line_txt('./working_with_files/work_files_copy/example.txt', 'this is one more test to test append text')