def Add(x,y):
    # iterate till no carry
    while y != 0:
        # carry now contain common bits of x and y
        carry = x & y

        # sum of bit of x and y where atleast one of bit is not set
        x = x ^ y

        # carry is shifted by one to left so that adding x gives desired output
        y = carry << 1
    return x
x = 10
y = 12
print(Add(x,y))




# def Add(x,y):
#     if y == 0:
#         return x
#     else:
#         return Add(x ^ y, (x & y) << 1)
# x = 10
# y = 12
# print(Add(x,y))
