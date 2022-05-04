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