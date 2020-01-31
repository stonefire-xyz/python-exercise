
def stringlist(str):
    stra=''
    strb=''
    for i in str.lower():
        if((i =='a')|(i =='e')|(i =='i')|(i =='o')|(i =='u')):
            stra=stra+i
        else:
            strb=strb+i
    print(stra)
    print(strb)

str='Hello wOrld!'
stringlist(str)        
print(str)
