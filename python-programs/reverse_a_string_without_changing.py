'''
input: my name is sonali
output: sonali is name my
'''
'''
"my name is sonali"
"my" "name"  "is"  "sonali"
 0       1      2       3
'''

# Time: O(N) and Space: O(1)

def covert_pos(strings):
    n = strings.split(" ")
    i, j = 0 , len(n) - 1
    while i < j:
        # print(i, j)
        n[i], n[j] = n[j], n[i]
        i += 1
        j -= 1
    print(" ".join(n))
strings = "my name is sonali"
covert_pos(strings)


