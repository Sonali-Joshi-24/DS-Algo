'''to find factorial of number recursion'''
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
# n = 5
# print(fact(n))

'''factorial of number iteractive'''
def fact(n):
    fact = 1
    if n < 0:
        return -1
    elif n == 0:
        return 1
    for i in range(1,n + 1):
        fact = fact * i
    return fact
n = 5
print(fact(n))
