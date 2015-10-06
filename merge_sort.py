c = [123,343,678,121,98,901,39,79]

def merge_sort(a):
	result = []
	if(len(a) < 2):
		return a
	b = a[:len(a)/2]
	c = a[len(a)/2:]
	
	x = merge_sort(b)
	y = merge_sort(c)

	i = 0	
	j = 0
	while i < len(x) and j < len(y):
		if x[i] > y[j]:
			result.append(y[j])
			j += 1
		else:
			result.append(x[i])
			i += 1
	result += x[i:]
	result += y[j:]

	return result

print merge_sort(c)
