def count_names(my_file):
    with open(my_file, 'r') as f:
        my_list = f.read().splitlines()
    return {n: my_list.count(n) for n in my_list}


print(count_names('nameslist.txt'))
