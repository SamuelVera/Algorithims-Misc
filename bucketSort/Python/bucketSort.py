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

def bucketSort(A: list, order: str = "asc"):
    """Do bucket sort to the given list A"""
    slot_num = 10 #Number of buckets
    arr = [] #Buckets

    for i in range(0, slot_num):
        #Initialize buckets
        arr.append([])

    for i in A: #Fill the buckets
        j = int(slot_num * i) #Index for bucket
        arr[j].append(i) #Put into bucket

    for i in range(0, slot_num): #Sort the buckets
        arr[i] = insertSort(arr[i], order) #Do insert sort over array and overload

    k = 0 #Pointer for return
    if order == "asc":
        for i in range(0, slot_num): #Build output array
            print(i)
            for j in range(0, len(arr[i])):
                A[k] = arr[i][j]
                k += 1
    else:
        for i in reversed(range(0, slot_num)): #Build output array
            for j in range(0, len(arr[i])):
                A[k] = arr[i][j]
                k += 1
    return A