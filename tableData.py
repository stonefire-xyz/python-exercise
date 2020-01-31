tableData=[['apple','orange','cherries','banana'],
	   ['Alice','Bob','Carol','David'],
	   ['dogs','cats','moose','goose']]
for i in range(3):
	for j in range(4):
                if (j == 3):
                    print(tableData[i][j].rjust(9))
                else:
                    print(tableData[i][j].rjust(9),end=' ')
for i in range(2):
    print(i)
		
