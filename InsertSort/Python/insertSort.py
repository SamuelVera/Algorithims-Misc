import sys #Import sys for script execution

def insertSort(arr: list, order: str = "asc") -> list:
    """Apply insert sort in the given order for the given array of integers
    
    -------------------
    Complexity:
        Time: O(n^2)
        Space: O(n) Array in memory
    -------------------
    Parameters:
    arr : list
        List to order
    order : "asc" | "desc"
        Order type, ascending or descending
    -------------------
    Returns:
    list
        Ordered list
    """
    cacheArr = arr.copy() #Cache array

    n = len(cacheArr) #List length

    #Actual algorithm
    for i in range(1, n): #Iterate from 1 to n - 1
        key = cacheArr[i] #Cache key
        j = i - 1 #Previous index
        if order == "asc": #Ascending order
            while j >= 0 and key < cacheArr[j]: #Iterate in reverse until spot is found
                cacheArr[j + 1] = cacheArr[j] #Move higher numbers up
                j -= 1 #Move reverse index a place
        else: #Descending order
            while j >= 0 and key > cacheArr[j]: #Iterate in reverse until spot is found
                cacheArr[j + 1] = cacheArr[j] #Move lower numbers up
                j -= 1 #Move reverse index a place

        cacheArr[j + 1] = key #Set key to position

    return cacheArr #Return ordered array

def tests():
    """Script testing"""
    list1 = []
    list2 = [2]
    list3 = [1,2,3,4,5]
    list4 = [5,4,3,2,1]
    list5 = [25,36,17,47,94,52,9,6,13]

    print("Order", list1, "Ascending...")
    print("Result", insertSort(list1, "asc"))
    print()
    print("Order", list1, "Descending...")
    print("Result", insertSort(list1, "desc"))
    print()
    print("Order", list2, "Ascending...")
    print("Result", insertSort(list2, "asc"))
    print()
    print("Order", list2, "Descending...")
    print("Result", insertSort(list2, "desc"))
    print()
    print("Order", list3, "Ascending...")
    print("Result", insertSort(list3, "asc"))
    print()
    print("Order", list3, "Descending...")
    print("Result", insertSort(list3, "desc"))
    print()
    print("Order", list4, "Ascending...")
    print("Result", insertSort(list4, "asc"))
    print()
    print("Order", list4, "Descending...")
    print("Result", insertSort(list4, "desc"))
    print()
    print("Order", list5, "Ascending...")
    print("Result", insertSort(list5, "asc"))
    print()
    print("Order", list5, "Descending...")
    print("Result", insertSort(list5, "desc"))
    print()

#Script execution
if __name__=="__main__":
    tests()
    sys.exit(0)