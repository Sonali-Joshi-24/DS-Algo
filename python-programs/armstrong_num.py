'''
what is armstrong num

153 --> true

1^3 = (1*1*1) = 1
5^3 = (5*5*5) = 125
3^3= (3*3*3) = 27

1+125+27 = 153
'''

'''armstrong number of 3number digit'''

def check_ArmStrong(nums):
    sums = 0
    temp = nums
    while temp > 0:
        # isolate the last digit
        last_digit = temp % 10

        # cube number n appen in sum
        sums += last_digit ** 3

        # remove the last_digit from temp
        temp = temp // 10
    if nums == sums:
        print("Armstrong")
    else:
        print("No")
nums = 370
check_ArmStrong(nums)


''' change ord to len of nums'''

# def check_ArmStrong(nums):
#     sums = 0
#     temp = nums
#     order = len(str(nums))
#     while temp > 0:
#         # isolate the last digit
#         last_digit = temp % 10

#         # cube number n appen in sum
#         sums += last_digit ** order

#         # remove the last_digit from temp
#         temp = temp // 10
#     if nums == sums:
#         print("Armstrong")
#     else:
#         print("No")
# nums = 1634
# check_ArmStrong(nums)


def armstrong(nums):
    temp = nums
    sums = 0
    while temp > 0:
        # take last digit
        last_digit = temp % 10
        sums += last_digit ** 3
        temp = temp // 10
    if nums == sums:
        print("armstrong")
    else:
        print("no")