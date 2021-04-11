import random #Random library

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

def quicksort(A: list, p: int, r: int, order: str="asc", randomized: bool=False):
    """Quick sort algorithm over the given array A
    
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
    randomized : bool
        Is randomized quicksort
    """
    if len(A) <= 1:
        return #No need to order
    if p < r:
        #Only continue if no pointers overlap
        #Calc q randomized or not
        q = partition(A, p, r, order) if randomized == False else randomizedPartition(A, p, r, order)
        
        #Do quick sort with sub arrays, keeping params
        quicksort(A, p, q - 1, order, randomized)
        quicksort(A, q + 1, r, order, randomized)