def selection(selectionList):
	for i in range(0, len(selectionList)):
		min = i
		for j in range(i+1, len(selectionList)):
			if selectionList[j] < selectionList[min]:
				min = j
		selectionList[i],selectionList[min] = selectionList[min],selectionList[i]
	print(selectionList)

if __name__ == '__main__':
    selectionList = [3, 4, 1, 2, 5, 8, 0]
    selection(selectionList)