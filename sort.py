a=[6,5,4,3,1,1]
for j in range(5):
    for i in range(5):
        if a[i] <= a[i+1]:
            continue
        else:
            k=a[i]
            a[i]=a[i+1]
            a[i+1]=k
print(a)
