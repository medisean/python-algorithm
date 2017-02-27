'''
	Merge sort algorithm in python. It's a Stable sort.
	Time complexity: O(nlogn)
	Space complexity: O(1)
'''

def merge_sort(lists):
	if len(lists) <= 1:
		return lists
	num = int(len(lists)/2)
	left = merge_sort(lists[:num])
	right = merge_sort(lists[num:])
	return merge(left, right)

def merge(left, right):
	l, r = 0, 0
	result = []
	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	result += right[r:]
	result += left[l:]
	return result

if __name__ == '__main__':
	print(merge_sort([2, 3, 1, 5, 4]))