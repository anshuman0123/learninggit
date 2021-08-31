a = []
for i in range(20):
    if i%2!=0:
        a.append(i)
    else:
        a.append('a')
b = [ ele if ele%2!=0 else 'a' for ele in range(20)]
#b is way more complicated
print(a)
print(b)