
'''iterative approch'''


def ispalindrome(nums):
    reverse = 0
    temp = nums
    while temp > 0:
        last_digit = temp % 10
        reverse = reverse * 10 + last_digit
        temp = temp // 10
    if reverse == nums:
        print("palindrome")
    else:
        print("not a palindrome")
nums = 1211
ispalindrome(nums)


