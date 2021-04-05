#Import the system for script execution
import sys

def binarySearch(sortedArr: list, x: int) -> int:
	"""Do a binary search on the given list

	Parameters:
	-------------
	sortedArr : list
		The sorted list of integers to make a search
	x : int 
		Integer to search
	Returns:
	-------------
	int
		The index if the given value is in the arlistray or -1 if else an integer
	"""
	#Initialize variables
	n = len(sortedArr) #List length

	if n == 0: #Validate list not empty
		return -1 #Nothing to search, nothing to find
	
	l = 0 #Initialize left
	r = len(sortedArr) - 1 #Initialize right

	#Keep running for base case
	while r >= l:
		mid = l + ((r - l)//2) #Calc mid placement

		if sortedArr[mid] == x: #Element index found
			return mid

		if sortedArr[mid] > x: #Divide to lower half
			r = mid - 1
		else: #Divide to upper half
			l = mid + 1

	return -1 #Nothing found

def tests():
	list1 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
	list2 = []
	list3 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

	print("Test 1", list1, "Search for", 34)
	print("Result", binarySearch(list1, 34))

	print()
	
	print("Test 2", list1, "Search for", 13)
	print("Result", binarySearch(list1, 13))
	
	print()

	print("Test 3", list1, "Search for", 1)
	print("Result", binarySearch(list1, 1))
	
	print()

	print("Test 4", list3, "Search for", 27)
	print("Result", binarySearch(list1, 27))
	
	print()

	print("Test 5", list3, "Search for", 700)
	print("Result", binarySearch(list1, 700))
	
	print()
	
	print("Test 6", list2, "Search for", 700)
	print("Result", binarySearch(list1, 700))

#Validate for script execution for testing
if __name__=='__main__':
	tests() #Execute tests
	sys.exit(0) #Exit code 0