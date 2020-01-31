
def split(m):
    pos=[]
    neg=[]
    for i in m:
        if(i <0):
            neg.append(i)
        elif(i >0):
            pos.append(i)
    print(pos)
    print(neg)
m=[3,1,-2,-4,1]
print(m)
split(m)
print(split(m))
