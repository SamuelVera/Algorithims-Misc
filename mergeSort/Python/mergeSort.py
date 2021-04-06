import sys #System import

def mergeSort(arr: list, order: str="asc"):
    """Apply merge sort mutating the given array
    Complexity:
    -----------------
    Time: 
        O(N*log(N))
    Space:
        S(N + N) #Array in memory + stack calls
    Parameters:
    -----------------
    arr : list
        Array of intergers to order
    order : str
        Order type: Ascending or descending (default = "asc")
    """
    if len(arr) > 1: #Stop the diving on single elements lists
        med = len(arr) // 2 #Calc medium point of array
        L = arr[:med] #Left half [0, med)
        R = arr[med:] #Right half [med, N)

        mergeSort(L, order) #Merge sort left
        mergeSort(R, order) #Merge sort right

        #Merging logic
        i = 0 #Left array pointer
        j = 0 #Right array pointer
        k = 0 #Original array pointer

        while i < len(L) and j < len(R): #Merge of two halfs
            if order == "asc": #Ascending order
                if L[i] < R[j]: #Left half item is lower
                    arr[k] = L[i] #Update merged with lower
                    i += 1 #Move left pointer
                else: #Right half item is lower
                    arr[k] = R[j] #Update merged with lower
                    j += 1 #Move right pointer
            else: #Descending order
                if L[i] > R[j]: #Left half item is higher
                    arr[k] = L[i] #Update merged with higher
                    i += 1 #Move left pointer
                else: #Right half item is higher
                    arr[k] = R[j] #Update merged with higher
                    j += 1 #Move right pointer
            k += 1 #Move original array pointer
        
        #Check for leftover elements
        while i < len(L): #Left half leftover
            arr[k] = L[i] #Add leftover
            i += 1 #Move left pointer
            k += 1 #Move original array pointer

        while j < len(R): #Right half leftover
            arr[k] = R[j] #Add leftover
            j += 1 #Move right pointer
            k += 1 #Move original array pointer

def tests():
    """Testing algorithm"""
    list1a = []
    list1b = []
    list2a = [1]
    list2b = [1]
    list3a = [4,3,2,10,12,1,5,6]
    list3b = [4,3,2,10,12,1,5,6]
    list4a = [38,27,43,3,9,82,10]
    list4b = [38,27,43,3,9,82,10]

    print("Ordering", list1a, "Ascending...")
    mergeSort(list1a)
    print("Result", list1a)
    print()
    print("Ordering", list1b, "Descending...")
    mergeSort(list1b, "desc")
    print("Result", list1b)
    print()
    print("Ordering", list2a, "Ascending...")
    mergeSort(list2a)
    print("Result", list2a)
    print()
    print("Ordering", list2b, "Descending...")
    mergeSort(list2b, "desc")
    print("Result", list2b)
    print()
    print("Ordering", list3a, "Ascending...")
    mergeSort(list3a)
    print("Result", list3a)
    print()
    print("Ordering", list3b, "Descending...")
    mergeSort(list3b, "desc")
    print("Result", list3b)
    print()
    print("Ordering", list4a, "Ascending...")
    mergeSort(list4a)
    print("Result", list4a)
    print()
    print("Ordering", list4b, "Descending...")
    mergeSort(list4b, "desc")
    print("Result", list4b)

if __name__=="__main__": #Validate script execution
    tests()
    sys.exit(0)