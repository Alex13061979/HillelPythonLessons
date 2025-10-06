x = int(input("Enter any 4-digit integer: "))

a = x // 1000
b = (x % 1000) // 100
c = (x % 100) // 10
d = x % 10

print(a)
print(b)
print(c)
print(d)