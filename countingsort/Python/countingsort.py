import math #Math module

def stringCountingSort(A: str, order: str = "asc") -> list:
    """Apply the countingsort algorithm to the given string"""

    B = [0]*len(A) #Output array
    C = [0]*256 #Counting array

    for char in A:
        C[ord(char)] += 1 #Frequency of each char

    for i in range(1, 256): #Count cumulative frequency
        j = i if order == "asc" else 255 - i #Index depending of the ordering type
        C[j] += C[j - 1] if order == "asc" else C[j + 1] #Accumulate depending on ordering type

    for i in range(0, len(A)):
        B[C[ord(A[i])] - 1] = A[i] #Build output array
        C[ord(A[i])] -= 1 #Reduce frequency

    return B

def integerCountingSort(A: list, order: str = "asc") -> list:
    """Apply countingsort algorithm to the given list"""

    maxInt = -math.inf #Max integer for C array
    
    for i in A:
        if maxInt < i:
            maxInt = i #New max

    maxInt += 1 #Account for indexes

    B = [0]*len(A) #Output array
    C = [0]*maxInt #Counting array

    for i in A:
        C[i] += 1 #Count frequency of each integer

    for i in range(1, maxInt): #Count cumulative frequency
        j = i if order == "asc" else maxInt - 1 - i #Index depending of the ordering type
        C[j] += C[j - 1] if order == "asc" else C[j + 1] #Accumulate depending on ordering type

    for i in range(0, len(A)):
        B[C[A[i]] - 1] = A[i] #Build output array
        C[A[i]] -= 1 #Reduce frequency

    return B