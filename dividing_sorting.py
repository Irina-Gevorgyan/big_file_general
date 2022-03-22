from main import file_rows_count

digits_big_file = open('numbers', 'r')

def dividing_sorting(file_name,ram_cap):
    file_name = open(file_name, 'w+')
    lines = []

    for i in range(0, ram_cap):
        line = digits_big_file.readline()

        if line != '':
            lines.append(int(line))

    lines.sort()

    for l in lines:
        file_name.write(f"{str(l)}\n")

    file_name.close()

###
ram_capacity = 200
count_of_files = int(file_rows_count / ram_capacity)

for count in range(count_of_files):
    dividing_sorting(f'file_{count}',ram_capacity)







