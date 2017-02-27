'''
	Select sort algorithm in python. Not a stable sort.
	Time complexity: O(n^2)
	Space complexity: O(1)
'''

def select_sort(lists):
	for i in range(len(lists)):
		index = i
		for j in range(i+1, len(lists)):
			# from small to big
			if lists[j] < lists[index]:
				index = j
		lists[i], lists[index] = lists[index], lists[i]
	return lists

if __name__ == '__main__':
	print(select_sort([2, 1, 3, 6, 4, 5, 9, 7, 8]))