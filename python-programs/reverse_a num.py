def reverse(nums):
    reverse = 0
    while nums > 0 :
        # isolate last digit
        last_digit = nums % 10

        # append the last digit to reverse
        reverse = reverse * 10 + last_digit

        # remove the last digit from num
        nums = nums // 10
    return reverse

nums = 123456
print(reverse(nums))


