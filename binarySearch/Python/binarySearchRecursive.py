import sys

def binarySearch(sortedArr: list, l: int, r: int, x: int) -> int:
    """Do a binary search recursively
    
    Parameters:
    -----------
    sortedArr : list
        Sorted array of integers
    
    l : int
        Left or lower border of interval

    r : int
        Right or upper border of interval

    x : int
        Number to search
    """
    #Check for base case
    if r >= l:
        #Search can still go on

        med = l + ((r - l) // 2) #Calculate medium

        if sortedArr[med] == x: #Element found
            return med #Return index
        
        if sortedArr[med] > x: #Divide intervel to lower half
            return binarySearch(sortedArr, l, med - 1, x)
        else :#Divide interval to upper half
            return binarySearch(sortedArr, med + 1, r, x)
    else: #Search done
        return -1 #Nothing found

def binarySearchWrapper(sortedArr: list, x: int) -> int: 
    """Wrapper for the binary search to get inital l and r, and validate empty"""
    #Array length
    n = len(sortedArr)

    if n == 0: #Empty list
        return -1 #Nothing to search

    return binarySearch(sortedArr, 0, n - 1, x) #Do recursively

def tests():
	list1 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
	list2 = []
	list3 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

	print("Test 1", list1, "Search for", 34)
	print("Result", binarySearchWrapper(list1, 34))

	print()
	
	print("Test 2", list1, "Search for", 13)
	print("Result", binarySearchWrapper(list1, 13))
	
	print()

	print("Test 3", list1, "Search for", 1)
	print("Result", binarySearchWrapper(list1, 1))
	
	print()

	print("Test 4", list3, "Search for", 27)
	print("Result", binarySearchWrapper(list1, 27))
	
	print()

	print("Test 5", list3, "Search for", 700)
	print("Result", binarySearchWrapper(list1, 700))
	
	print()
	
	print("Test 6", list2, "Search for", 700)
	print("Result", binarySearchWrapper(list1, 700))

#Validate for script execution for testing
if __name__=='__main__':
	tests() #Execute tests
	sys.exit(0) #Exit code 0