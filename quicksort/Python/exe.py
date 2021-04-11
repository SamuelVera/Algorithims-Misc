import sys #System
import quicksort #Quicksort

if __name__=="__main__":
    #Script execution
    listA1 = []
    listA2 = []
    listB1 = [1]
    listB2 = [1]
    listC1 = [2, 5, 12, 3, 4, 10, 2, 6]
    listC2 = [2, 5, 12, 3, 4, 10, 2, 6]
    listD1 = [22, 500, 12, 33, 45, 10, 2, 26]
    listD2 = [22, 500, 12, 33, 45, 10, 2, 26]

    print("Sorting", listA1, "Ascending")
    quicksort.quicksort(listA1, 0, len(listA1) - 1, "asc", False)
    print("Result:", listA1)
    print()
    print("Sorting", listA2, "Descending (Random pivot)")
    quicksort.quicksort(listA2, 0, len(listA2) - 1, "desc", True)
    print("Result:", listA2)
    print()
    print("Sorting", listB1, "Ascending")
    quicksort.quicksort(listB1, 0, len(listB1) - 1, "asc", False)
    print("Result:", listB1)
    print()
    print("Sorting", listB2, "Descending (Random pivot)")
    quicksort.quicksort(listB2, 0, len(listB2) - 1, "desc", True)
    print("Result:", listB2)
    print()
    print("Sorting", listC1, "Ascending")
    quicksort.quicksort(listC1, 0, len(listC1) - 1, "asc", False)
    print("Result:", listC1)
    print()
    print("Sorting", listC2, "Descending (Random pivot)")
    quicksort.quicksort(listC2, 0, len(listC2) - 1, "desc", True)
    print("Result:", listC2)
    print()
    print("Sorting", listD1, "Ascending")
    quicksort.quicksort(listD1, 0, len(listD1) - 1, "asc", False)
    print("Result:", listD1)
    print()
    print("Sorting", listD2, "Descending (Random pivot)")
    quicksort.quicksort(listD2, 0, len(listD2) - 1, "desc", True)
    print("Result:", listD2)
    print()

    sys.exit(0) #Exit code