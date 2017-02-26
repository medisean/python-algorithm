'''
	Bubble sort in python
	Time complexity: O(n^2)
	Space complexity: O(0)
'''

def bubble_sort(lists):
	for i in range(len(lists)):
		for j in range(i+1, len(lists)):
			# frome small to big
			if lists[i] > lists[j]:
				lists[i], lists[j] = lists[j], lists[i]
	return lists

if __name__ == '__main__':
	print(bubble_sort([2, 3, 5, 1, 4]))