'''
prime number always gretaer than 1

'''


def isprime(nums):
    flag = False
    # prime number is always greater then 1
    if nums > 1:
        for i in range(2, nums):
            # check for factors
            if nums % i == 0:
                flag = True
                break
    if flag:
        print("num is not prime")
    else:
        print("nums is prime")
nums = 8
isprime(nums)


