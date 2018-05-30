def InsertSort(InsertList):
	for i in range(1,len(InsertList)):
		for j in range(i,0,-1):
			print(j)
			if InsertList[j] < InsertList[j-1]:
				InsertList[j],InsertList[j-1] = InsertList[j-1],InsertList[j]
	print(InsertList)
 
if __name__ == '__main__':
    InsertList = [3, 4, 1, 2, 5, 8, 0]
    InsertSort(InsertList)
