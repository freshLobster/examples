def average(a):
	index = len(a)
	avg = 0
	while index > 0:
		avg = avg + a[index-1]
		index = index - 1
	avg = avg/len(a)
	return avg

def maximum(a):
	index = len(a)
	m = 0
	while index > 0:
		if m < a[index-1]:
			m = a[index-1]
		index = index-1
	return m

nums = []
while True:
	nums.append(float(raw_input('type a number:')))
 	if 'n' == raw_input('continue?(y/n): '):
 		break
print 'average: ', average(nums)
print 'max: ', maximum(nums)