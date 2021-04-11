def bubblesort(A: list, order: str="asc"):
    """Apply bubble sort to the given integers list
    
    Parameters
    -----------------
    A : list
        List to order
    order : str
        Order type. "asc" or "desc"
    """
    n = len(A) #Array size

    for i in range(0, n): #Iterate elements
        for j in range(0, n - i - 1): #Iterate other elements
            if order == "asc": #Ascending order
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j] #Swap
            else: #Descending order
                if A[j] < A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j] #Swap