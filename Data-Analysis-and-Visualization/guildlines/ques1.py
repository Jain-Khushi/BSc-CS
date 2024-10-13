dic1 = {'Boys': [72, 68, 70, 69, 74], 'Girls': [63, 65, 69, 62, 61]}
print("original:",dic1)
l = [] 
key = []
temp = []
for i in dic1:
    key.append(i)
    temp.append(dic1[i])

for i in range(len(temp[0])):
    dic2 = {}
    k = 0
    for j in key:
        dic2[j] = temp[k][i]
        k = k+1
    l.append(dic2)
print("Output:\n", l)
