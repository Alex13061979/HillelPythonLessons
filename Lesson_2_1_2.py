a, b, c, d = input("Enter any 4-digit integer: ")
y = int(a)
u = int(b)
v = int(c)
w = int(d)

div, mod = divmod(w, v)
div1, mod1 = divmod(u, y)

print(div)
print(mod)
print(div1)
print(mod1)
