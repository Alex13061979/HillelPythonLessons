lst = [55, 17, 7, 11, 0,  3]
x = len(lst)
# print(x)
r = range(0, x, 2)
# print(r)
even_index_elem = []
for i in r:
    value = lst[i]
    even_index_elem.append(value)
# print(even_index_elem)
eil_sum = sum(even_index_elem)
# print(eil_sum)
d = lst[-1]
# print(d)
result = eil_sum * d
print(result)


