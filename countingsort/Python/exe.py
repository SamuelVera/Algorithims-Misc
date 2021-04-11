import sys #System import
import countingsort

if __name__=="__main__":
    stringA = "helloworld"
    stringB = "theworldisfvcked"
    stringC = "palomocojo"
    list1 = [22, 500, 12, 33, 45, 10, 2, 26]
    list2 = [2, 5, 12, 12, 3, 4, 10, 2, 6]

    print("Ordering string descending:", stringA)
    print("Result:", countingsort.stringCountingSort(stringA, "desc"))
    print()
    print("Ordering string ascending:", stringB)
    print("Result:", countingsort.stringCountingSort(stringB))
    print()
    print("Ordering string descending:", stringC)
    print("Result:", countingsort.stringCountingSort(stringC, "desc"))
    print()
    print("Ordering list", list1)
    print("Result:", countingsort.integerCountingSort(list1))
    print()
    print("Ordering list descending", list2)
    print("Result:", countingsort.integerCountingSort(list2, "desc"))
    print()

    sys.exit(0) #Exit execution