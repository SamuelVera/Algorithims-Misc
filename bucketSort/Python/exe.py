import sys #System import
import bucketSort

if __name__=="__main__":
    #Script execution
    list1 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    list2 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

    print("Ordering", list1)
    print("Result:", bucketSort.bucketSort(list1))
    print()
    print("Ordering", list1, "descending")
    print("Result:", bucketSort.bucketSort(list2, "desc"))
    print()

    sys.exit(0) #Exit execution