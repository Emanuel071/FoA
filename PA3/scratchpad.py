A ="101"
B ="01"
S = "10011011"
    
m = len(A)            # A is down the rows, indexed by i, starting 1
n = len(B)            # B goes across cols, indexed by j, starting 1
s = len(S)

total = m + n
print(s)
print(total)
i = 0

while s != total or i < 10:
    A_new = A*2
    total = len(A_new) + n
    if total == s:
        A = A_new
        m = len(A) 
        break
    B_new = B*2
    total = m + len(B_new)
    if total == s:
        B = B_new
        break
    if total > s:
        break
    print(i)
    i += 1

print(A)
print(B)

