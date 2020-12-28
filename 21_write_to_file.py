def write_file(output_file):
    output_file = output_file + '.txt'
    with open(output_file, 'a') as f:
        f.write('Write this down\n')


def name_it():
    output_file = '_'.join(input('Enter name of your file: ').lower().split(' '))
    write_file(output_file)


name_it()