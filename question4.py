def swap_value(a, b):
    a, b = b, a
    return a, b


a = 5
b = 10

a ,b = swap_value(a, b)

print(a )
print(b )