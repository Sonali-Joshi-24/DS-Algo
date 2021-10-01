

'''print fibonacci series of number
itrative method'''

def fibbo(num):
    first, second = 0 , 1
    for i in range(0,num):
        if i <= 1:
            result = i
        else:
            result = first + second
            first = second
            second = result
        print(result)
num = 5
fibbo(num)