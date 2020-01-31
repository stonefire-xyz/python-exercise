
while True:
    print('enter an a number:' )
    ok=input()
    if ok=='q':
        break
    else:
        sum=0
        N=int(ok)+1
        for i in range(N):
            sum=sum+i
        print('you want number is ',sum)

