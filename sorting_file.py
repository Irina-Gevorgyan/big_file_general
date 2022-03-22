from dividing_sorting import count_of_files

first_numbers = []
files = []
min_value = 0

sorted_file = open('sorted_file', 'w+')

for i in range(count_of_files):
    file_i = open(f'file_{i}','r')
    files.append(file_i)
    first_numbers.append(int(file_i.readline()))

for row in range(4000):

    min_value = min(first_numbers)
    min_file = first_numbers.index(min_value)

    next_elem = files[min_file].readline()

    if next_elem != '':
        first_numbers[min_file] = int(next_elem)
    else:
        first_numbers[min_file] = 11_000


    sorted_file.write(f"{str(min_value)} \n")

sorted_file.close()

