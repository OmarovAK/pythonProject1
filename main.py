import os

path = os.path.join(os.getcwd(), '1.txt')
path_two = os.path.join(os.getcwd(), '2.txt')
path_three = os.path.join(os.getcwd(), '3.txt')

my_list = []
with open(path, encoding='utf-8') as file, open(path_two, encoding='utf-8') as file_two, open(path_three, encoding='utf-8') as file_three:
    for i in file.readlines(), file_two.readlines(), file_three.readlines():
        file_name_one = os.path.basename(path)
        file_name_two = os.path.basename(path_two)
        file_name_three = os.path.basename(path_three)
        my_list.append(i)
    count = 1
    for k in my_list:
        k.insert(0, str(len(k)))
        if count == 1:
            k.insert(0, file_name_one)
        if count == 2:
            k.insert(0, file_name_two)
        if count == 3:
            k.insert(0, file_name_three)
        count += 1


new_list = []

list_len_my_list = []


for i in my_list:
    list_len_my_list.append(len(i))

list_len_my_list.sort()

for i in list_len_my_list:
    for k in my_list:
        if i == len(k):
            new_list.append(k)

path = os.path.join(os.getcwd(), 'result.txt')

with open(path, mode='w') as file_one:
    pass

with open(path, mode='a') as file:
    for i in new_list:
        for k in i:
            file.writelines(k.strip() + '\n')
        file.writelines('\n')











