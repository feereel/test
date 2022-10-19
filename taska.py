
a1 = [int(i) for i in input().split()]
a2 = [int(i) for i in input().split()]
a3 = [int(i) for i in input().split()]
l = [a1[0],a2[0],a3[0]]

al = set(a1+a2+a3)

a1 = a1[1:]
a2 = a2[1:]
a3 = a3[1:]

mn1 = []
if a1[-1] == a2[0]:
    mn1 = a1+a2[1:]
elif a2[-1] == a1[0]:
    mn1 = a2+a1[1:]

mn2 = []
if a2[-1] == a3[0]:
    mn2 = a2+a3[1:]
elif a3[-1] == a2[0]:
    mn2 = a3+a2[1:]

mn3 = []
if a1[-1] == a3[0]:
    mn3 = a1+a3[1:]
elif a3[-1] == a1[0]:
    mn3 = a3+a1[1:]

mn4 = []
mn5 = []
mn6 = []
mn7 = []
mn8 = []
mn9 = []

if a1[-1] == a2[0] and a2[-1] == a3[0]:
    mn4 = a1+a2[1:]+a3[1:]
if a1[-1] == a3[0] and a3[-1] == a2[0]:
    mn5 = a1+a3[1:]+a2[1:]
if a2[-1] == a1[0] and a1[-1] == a3[0]:
    mn6 = a2+a1[1:]+a3[1:]
if a2[-1] == a3[0] and a3[-1] == a1[0]:
    mn7 = a2+a3[1:]+a1[1:]
if a3[-1] == a1[0] and a1[-1] == a2[0]:
    mn8 = a3+a1[1:]+a2[1:]
if a3[-1] == a2[0] and a2[-1] == a1[0]:
    mn9 = a3+a2[1:]+a1[1:]

am = [mn1,mn2,mn3,mn4,mn5,mn6,mn7,mn8,mn9,a1,a2,a3]

res = []

for m in am:
    k = 0
    for i in range(len(m)):
        if m[i:i+len(a1)] == a1:
             k += 1
             break

    for i in range(len(m)):
        if m[i:i+len(a2)] == a2:
             k += 1
             break

    for i in range(len(m)):
        if m[i:i+len(a3)] == a3:
             k += 1
             break

    if k == 3:
        res.append(m)
        

ans = []

if len(res) > 0:
    ans = res[0]

for m in res:
    if len(m) < len(ans):
        ans = m


print(len(ans))
print(*ans)
