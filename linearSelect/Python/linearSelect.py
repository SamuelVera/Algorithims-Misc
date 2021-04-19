import math #Math module
import random #Random module

def maxMin(A: list, t: str="max") -> int:
    """Get max or min from given array
    
    Parameters:
    ---------------
    A : list
        Array of elements
    t : str
        Type of search, max or min

    Returns:
    ---------------
        Desired element
    """
    m = -math.inf if t == "max" else math.inf #Initialize -inf or + inf depending on the case
    for i in A:
        if t == "max":
            #Searching max
            if m < i:
                m = i #Replace
        else:
            #Searching min
            if m > i:
                m = i #Replace
    return m

def partition(A: list, p: int, r: int, order: str="asc") -> int:
    """Partition algorithm for the quicksort algorithm
    
    Parameters:
    ---------------
    A : list
        Array to order
    p : int
        Lower limit of array
    r : int
        Upper limit of array
    order : str
        Order type
    
    Returns:
    ---------------
    int
        Calculated partition for sub arrays
    """
    pivot = A[r] #Pivot
    i = p - 1 #i pointer
    
    for j in range(p, r): #Iterate j from lower limit to upper limit

        if order=="asc": #Ascending order
            if A[j] <= pivot: #If current element is lower than the pivot
                i+=1 #Move i pointer
                A[i], A[j] = A[j], A[i] #Swap i and j
        else: #Descending order
            if A[j] >= pivot: #If current element is higher than the pivot
                i+=1 #Move i pointer
                A[i], A[j] = A[j], A[i] #Swap i and j
    
    #Swap i + 1 with upper limit
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1 #Return q

def randomizedPartition(A: list, p: int, r: int, order: str="asc"):
    """Randomized selection for pivot
    
    Parameters:
    --------------
    A : list
        Array to order
    p : int
        Lower limit of array
    r : int
        Upper limit of array
    order : str
        Order type
    """
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i] #Swap pivot
    q = partition(A, p, r, order) #Calculate partition
    return q #Return partition index

def randomizedSelect(A: list, p: int, r: int, i: int) -> int:
    """Search of item with randomized select"""
    if p == r:
        #Reached the desired element
        return A[p]

    q = randomizedPartition(A, p, r) #Randomize partitions
    k = q - p + 1

    #Search in ascending order
    if i == k:
        #q is desired element
        return A[q]
    elif i < k:
        #Divide to the right
        return randomizedSelect(A, p, q - 1, i)
    else:
        #Divide to the left
        return randomizedSelect(A, q + 1, r, i - k)

def insertSort(A: list, p: int, r: int, order: str = "asc") -> list:
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

    if p > r: #Validate
        return

    #Actual algorithm
    for i in range(p, r): #Iterate from 1 to n - 1
        key = A[i] #Cache key
        j = i - 1 #Previous index
        if order == "asc": #Ascending order
            while j >= 0 and key < A[j]: #Iterate in reverse until spot is found
                A[j + 1] = A[j] #Move higher numbers up
                j -= 1 #Move reverse index a place
        else: #Descending order
            while j >= 0 and key > A[j]: #Iterate in reverse until spot is found
                A[j + 1] = A[j] #Move lower numbers up
                j -= 1 #Move reverse index a place

        A[j + 1] = key #Set key to position