def file_overlap(file1, file2):
    with open(file1, 'r') as f:
        lst1 = f.read().splitlines()
    with open(file2, 'r') as f:
        lst2 = f.read().splitlines()
    return [n for n in lst1 if n in lst2]


print(file_overlap('primenumbers.txt', 'happynumbers.txt'))
