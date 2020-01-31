def sort(a=[]):
    for j in range(len(a)-1):
        for i in range(len(a)-1):
            if a[i] <= a[i+1]:
                continue
            else:
                k=a[i]
                a[i]=a[i+1]
                a[i+1]=k
    return(a)
print("Enter you list to sort:",end='')
listinput = input()
list=listinput.split(",")
for i in range(len(list)):
    list[i]=int(list[i])
sort(list)
print(list)
