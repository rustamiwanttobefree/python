var_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
var = 0
while i < var_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[var], my_list[var+ 1] = my_list [var + 1], my_list[var]
        el += 2
print(my_list) 