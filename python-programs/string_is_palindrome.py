def pali(stri):
    y = ""
    for i in stri:
        y = i + y
    if stri == y:
        print("palindrome")
    else:
        print("no")
stri = "madame"
pali(stri)