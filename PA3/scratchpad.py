'''
A ="101"
B ="01"
S = "000010011011"
    
m = len(A)            # A is down the rows, indexed by i, starting 1
n = len(B)            # B goes across cols, indexed by j, starting 1
s = len(S)

print(S)

print(S[0])
print(type(S[0]))

# print(S[0])
while S[0] == "0":
    S = S[ 1 : :]
    if S[0] == "1":
        break
    


print(S)
'''

A ="101"
B ="01"
S = "1001110110011"
    
m = len(A)            # A is down the rows, indexed by i, starting 1
n = len(B)            # B goes across cols, indexed by j, starting 1
s = len(S)

# adds total         
total = m + n
# need this for the later algorithm
i = 2

print("here: " + A + " " + B)

n_new = n
m_new = m

# algorithm to add the A's on the matrix for more interleaving 
while s != total or i < 10:
    A_new = A*i                 # concatinates A
    total = len(A_new) + n_new      # new total length
    if total == s:              # is the total equal to S?
        A = A_new               # if so make A new A
        m = len(A)              # replace with new length
        print("hey")
        break                   # end loop
    B_new = B*i                 # same pattern above below
    total = m_new + len(B_new)
    if total == s:
        B = B_new
        n = len(B) 
        print("there")
        if i != 2:
            A = A_new               # if so make A new A
            m = len(A)              # replace with new length
        break
    m_new = len(A_new)
    n_new = len(B_new) 
    print("here: " + A_new + " " + B_new)
    if total > s:               # breaks if total is bigger than
        break                   # length of s
    i += 1
# see write up above i am aware that this is not at all efficient 
# algorithm to processing the string. 
print("hey: " + A_new + " " + B_new)
 
'''
print(S)

print(S[s-1])
print(S[ : (s-1)])
print(type(S[s-1]))

i = 1
# print(S[0])
while S[s-1] == "0":
    S = S[: (s-1)]
    s = len(S)
    if S[s-1] == "1":
        break


print(S)
'''

'''
total = m + n
print(s)
print(total)
i = 0

# while s != total or i < 10:
#     A_new = A*2
#     total = len(A_new) + n
#     if total == s:
#         A = A_new
#         m = len(A) 
#         break
#     B_new = B*2
#     total = m + len(B_new)
#     if total == s:
#         B = B_new
#         n = len(B) 
#         break
#     if total > s:
#         break
#     print(i)
#     i += 1

# print(A)
# print(m)
# print(B)
# print(n)
'''