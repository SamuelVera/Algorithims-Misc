import sys #System
import heapsort

if __name__=="__main__":
    #Script execution

    list1 = []
    list2 = [1]
    list3 = [2, 5, 12, 3, 4, 10, 2, 6]
    list4 = [22, 500, 12, 33, 45, 10, 2, 26]

    print("Ordering", list1, "Ascending")
    print("Result", heapsort.heapsort([]))
    print("Ordering", list1, "Descending")
    print("Result", heapsort.heapsort([], "desc"))
    print()
    print("Ordering", list2, "Ascending")
    print("Result", heapsort.heapsort([1]))
    print("Ordering", list2, "Descending")
    print("Result", heapsort.heapsort([1], "desc"))
    print()
    print("Ordering", list3, "Ascending")
    print("Result", heapsort.heapsort([2, 5, 12, 3, 4, 10, 2, 6]))
    print("Ordering", list3, "Descending")
    print("Result", heapsort.heapsort([2, 5, 12, 3, 4, 10, 2, 6], "desc"))
    print()
    print("Ordering", list4, "Ascending")
    print("Result", heapsort.heapsort([22, 500, 12, 33, 45, 10, 2, 26]))
    print("Ordering", list4, "Descending")
    print("Result", heapsort.heapsort([22, 500, 12, 33, 45, 10, 2, 26], "desc"))
    print()


    sys.exit(0) #Exit operation