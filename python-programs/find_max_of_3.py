def find_max(n1,n2,n3):
    if n1 >= n2 and n1 >= n3:
        print("n1 is greatest")
    if n2 >= n1 and n2 >= n3:
         print("n2 is greatest")
    if n3 >= n1 and n3 >= n2:
        print("n3 is greatest")
n1, n2 ,n3 = 1,4,6
find_max(n1,n2,n3)

