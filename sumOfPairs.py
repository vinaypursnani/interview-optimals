# Given an array find values that add up to give the targetSum
# Provided that the array is sorted this can be done in nlogn
# rather than going for n^2 with 2 for loops

my_hash = {}
def sumOfPairsOp(array, targetSum):
	for i in array:
		if targetSum-i in my_hash:
			return [i,targetSum-i]
		else:
			my_hash[i] = True
			# print(my_hash)
	return []

arr = ([-2,-1,1,2,45,55,110,125])
# print(arr)
print(sumOfPairsOp(arr,100))
