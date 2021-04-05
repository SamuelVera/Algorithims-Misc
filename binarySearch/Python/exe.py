import sys #System import
import binarySearch #Normal binary search module import
import binarySearchRecursive #Recursive binary search moduel import

#Validate for script execution for testing
if __name__=='__main__':
    
    print("Normal binary search")
    binarySearch.tests() #Execute tests for binary search

    print()
    print("------------------------------------")
    print()
    
    print("Recursive binary search")
    binarySearchRecursive.tests() #Execute tests for binary search
	
    sys.exit(0) #Exit code 0