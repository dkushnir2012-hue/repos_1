num_list = [1, 5, 2, 8, 3, 7]

max_num = num_list[0]
for num in num_list:
    if num > max_num:
        max_num = num
print(max_num)

min_num = num_list[0]
for num in num_list:
    if num < min_num:
        min_num = num
print (min_num)

total = 0
for num in num_list:
    total = total + num
print (total)

marks = [10, 8, 12, 7, 9]

tale = len(marks)
total_marks = 0
for mark in marks:
    total_marks = total_marks + mark
middle = total_marks / tale
print(middle)

for mark in marks:
    if mark > middle:
        print(mark)