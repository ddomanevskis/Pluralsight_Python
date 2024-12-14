import json


def read_print_json(fn, pretty, sort):
    with open(fn) as json_file:
        data = json.load(json_file)
        print(json.dumps(data, indent=4, sort_keys=sort if pretty else data))


def update_author_json(fn, arr_name, pos, key, val):
    with open(fn, 'r') as read_file:
        data = json.load(read_file)
        data[arr_name][pos][key] = val
        with open(fn, 'w') as write_file:
            json.dump(data, write_file)


read_print_json(
    './working_with_files/work_files_copy/authors.json',
    False,
    False
)
update_author_json(
    './working_with_files/work_files_copy/authors.json',
    'authors',
    0,
    'name',
    'John Doe')
