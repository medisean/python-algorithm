'''
	Quick sort in python. Quick sort is not stable.
	Time complexity: O(nlogn)
	Space complexity: O(log2n)
'''

def quick_sort(lists, left, right):
	if left >= right:
		return lists

	first = left
	last = right
	key = lists[first]

	while first < last:
		while first < last and lists[last] >= key:
			last = last - 1
		lists[first] = lists[last]

		while first < last and lists[first] <= key:
			first = first + 1
		lists[last] = lists[first]
	lists[first] = key

	quick_sort(lists, left, first-1)
	quick_sort(lists, last+1, right)

	return lists

if __name__ == '__main__':
	lists = [3, 2, 1, 5, 4]
	print(quick_sort(lists, 0, len(lists) - 1))