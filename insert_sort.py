'''
	The insert sort algorithm in python.
	Time complexity: O(n^2)
	Space Complexity: O(n)
'''

def insertSort(lists):
	result = []
	for item in lists:
		if len(result) == 0:
			result.append(item)
			continue

		# find the right position
		position = 0
		flag = False
		for index in range(len(result)):
			# from big to small use >, or use <
			position = index
			if item < result[index]:
				flag = True
				break

		# insert item to array
		if flag:
			result.insert(position, item)
		else:
			result.append(item)



	return result

if __name__ == '__main__':
	print(insertSort([2, 1, 5, 3, 4]))
	print(insertSort([3, 5, 4, 8, 7]))