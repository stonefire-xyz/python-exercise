import os
totalSize=0
for filename in os.listdir('/home/killer'):
	totalSize=totalSize + os.path.getsize(os.path.join('/home/killer',filename))
print(totalSize)
