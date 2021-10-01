'''
Time: O(N) and Space: O
reverse k char and skip k char

k = 2
str = abcdefg
output = bacdfeg

'''
def reverse(string):
    c = ''
    for i in range(len(string) - 1, -1, -1):
        c = c + string[i]
    return c

def reverse_str(s, k):
    s =  list(s)
    for i in range(0,len(s), 2*k):
        s[i:i+k] = reverse(s[i:i+k])
    return "".join(s)


string = "abcdefg"
k = 2
print(reverse_str(string,k))


'''explanation of 2*K:   L is pointing to beginning of k characters to be be reversed.
 Then we have to skip k characters, i.e., 
next k characters should not be reversed. 
So, to skip next k characters, we advance by 2k instead of k.'''