import sys #System import
import linearSelect #Linear select

if __name__=="__main__":
    list1 = [2, 5, 4, 3, 9, 10, 13, 15]
    search1 = 6
    search2 = 7
    print("Searching", search1, "in", list1)
    print("Result", linearSelect.randomizedSelect(list1, 0, len(list1) - 1, search1))
    print("Searching", search2, "in", list1)
    print("Result", linearSelect.randomizedSelect(list1, 0, len(list1) - 1, search2))

    sys.exit(0) #Exit execution