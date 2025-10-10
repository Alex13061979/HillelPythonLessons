# Case1: The list is empty
first_list = []
sub_list1 = first_list[:0]
sub_list2 = first_list[0:]

print(sub_list1)
print(sub_list2)

second_list = [sub_list1, sub_list2]
print(second_list)