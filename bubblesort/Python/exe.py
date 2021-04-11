import sys
import bubblesort

if __name__=="__main__":
    list1 = []
    list2 = [2]
    list3 = [1,2,3,4,5]
    list4 = [5,4,3,2,1]
    list5 = [25,36,17,47,94,52,9,6,13]

    print("Ordering", list1)
    bubblesort.bubblesort(list1)
    print("Result:", list1)
    print()
    print("Ordering", list2)
    bubblesort.bubblesort(list2)
    print("Result:", list2)
    print()
    print("Ordering", list3, "Descending")
    bubblesort.bubblesort(list3, "desc")
    print("Result:", list3)
    print()
    print("Ordering", list4, "Ascending")
    bubblesort.bubblesort(list4)
    print("Result:", list4)
    print()
    print("Ordering", list5, "Descending")
    bubblesort.bubblesort(list5, "desc")
    print("Result:", list5)
    print()
    sys.exit()