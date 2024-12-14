import csv


def read_csv(fn, delimeter):
    with open(fn) as csv_f:
        cnt = -1
        rows = csv.reader(csv_f, delimiter=delimeter)
        for r in rows:
            if cnt == -1:
                print(f'{" | ".join(r)}')
            else:
                print(f'{r[0]} | {r[1]} | {r[2]} | {r[3]}')
            cnt += 1
        print(f'{cnt} lines')


def write_csv(fn, header, row):
    with open(fn, mode='w', newline='') as csv_f:
        writer = csv.writer(csv_f, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(row)


read_csv(
    './working_with_files/work_files_copy/names.csv',
    ',')
write_csv(
    './working_with_files/work_files_copy/names.csv',
    ['name', 'surname', 'age', 'sex'],
    ['John', 'Doe', 30, 'male'])
