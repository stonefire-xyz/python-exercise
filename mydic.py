mycomputer={
        'cpu':'amd',
        'motherboard':'gigabyte'
        }
print(mycomputer['cpu']) 
print(mycomputer['motherboard'])
print(len(mycomputer))
mycomputer['mouse']='wireless'
for item in mycomputer:
    print(item,mycomputer[item])
