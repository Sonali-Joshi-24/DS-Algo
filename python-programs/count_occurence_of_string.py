def count_occurence(string, char):
    count = 0
    for i in range(len(string)):
        if string[i] == char:
            count += 1
    return count
string , char  = "saurabh" , "a"
print(count_occurence(string, char))