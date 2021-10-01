# given two linklist u need to merge both inplace  in sorted order
# Time: O(n + m) ...where n and m are the len of list 
# Space: O(1)

from Linklist import l,v,r

a = [1,2,3,5]
[l.insert(i) for i in a]
    
b = [4,6,9,10,11,81]
[v.insert(j) for j in b]



def mergeTwoList(l,v):
    # base case

    if not l:
        v.display()
        return
    if not v:
        l.display()
        return
    h1 , h2 = l.getHead(), v.getHead()
    ans = []


    while h1 != None:
        ans.append(h1.data)
        h1 = h1.next
    while h2 != None:
        ans.append(h2.data)
        h2 = h2.next

    ans.sort()
    [r.insert(i) for i in ans]
    r.display()

# mergeTwoList(l,v)

'time: O(N) and Space: O(1)'

def optimized(l,v):
    p1 = l.getHead() 
    p2 = v.getHead()
    p3 = None

    while p1 is not None and p2 is not None:
        if p1.data < p2.data:
            p3 = p1
            p1 = p1.next
        else:
            if p3 is not None:
                p3.next = p2
            p3 = p2
            p2 = p2.next
        
        if p1 is None:
            p3.next = p2
    l.head = l.getHead() if l.getHead().data < v.getHead().data else v.getHead()
    l.display()
optimized(l,v)