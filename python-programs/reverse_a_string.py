'''
input: sonali
output: ilanos
'''


''' 1st way to reverse a string  '''

# def reverse_str(strings):
#     reverse_string = strings[::-1]
#     print(reverse_string)
# strings = "sonali"
# reverse_str(strings)


''' 2nd way to reverse a string '''

# def reverse_str(strings):
#     stri = " "
#     for i in strings:
#         stri = i + stri
#     return stri
# strings = "saurabh"
# print(reverse_str(strings))



''' 3rd ways using join '''

# def reverse_str(strings):
#     return "".join(reversed(strings))
# strings = "omkar"
# print(reverse_str(strings))

def reverse(string):
    char =" "
    for i in (string):
        char = i + char
    return char
print(reverse("sonali"))