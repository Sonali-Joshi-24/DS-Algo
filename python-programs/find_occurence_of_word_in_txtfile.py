text = open("sample.txt", "r")

d = dict()

# loop through each line
for line in text:
    line = line.strip()

    # convert all char in lowercase to avoid mismatch
    line = line.lower()

    # split line into words
    words = line.split(" ")

    # iterate over each word in line
    for w in words:
        # if word in dict
        if w in d:
        # incr count of word by 1
            d[w] = d[w] + 1
        else:
            d[w] = 1

# for print key val
for key in list(d.keys()):
    print(key, ":" , d[key])


    
