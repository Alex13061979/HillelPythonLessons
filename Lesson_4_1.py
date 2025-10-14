# Початковий список
lst1 = [7, 0, 10, 65, 0, 4, 8]
lst_wt_zero = []
for i in lst1:
    if i != 0:
        lst_wt_zero.append(i)
zero_count = lst1.count(0)
new_lst1 =lst_wt_zero +[0] * zero_count
print(new_lst1)