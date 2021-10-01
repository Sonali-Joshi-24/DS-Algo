# def anagram(s1 , s2):
#     assert len(s1) == len(s2), f'the string {s1} and {s2} len varies hence not anagram'

#     if set(s1.lower()) == set(s2.lower()):
#         print("anagram")
#     else:
#         print("not an anagram")

# s1 = "sonalie"
# s2 = "saloni"
# anagram(s1,s2)



def anagram(s1, s2):
    assert len(s1) == len(s2), f'the string {s1} and {s2} are not equal'

    if set(s1.lower()) == set(s2.lower()):
        print("Anagram") 

    else:
        print("no")
str1 = "Race"
str2 = "Care"
anagram(str1,str2)
# # convert both the strings into lowercase
# str1 = str1.lower()
# str2 = str2.lower()

# # check if length is same
# if(len(str1) == len(str2)):

#     # sort the strings
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)

#     # if sorted char arrays are same
#     if(sorted_str1 == sorted_str2):
#         print(str1 + " and " + str2 + " are anagram.")
#     else:
#         print(str1 + " and " + str2 + " are not anagram.")

# else:
#     print(str1 + " and " + str2 + " are not anagram.")