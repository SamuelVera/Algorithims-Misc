class BinaryHeap:
    """Binary heap implementation for integers"""
    size = 0
    isMax = False

    def make_heap(self):
        self.size = 0 #Size 0

    def __init__(self):
        """Constructor"""
        self.make_heap()

    def heapify(self, A: list, i: int):
        """Heapify the given array"""
        left = 2*i
        right = (2*i) + 1
        heapIndex = i

        if self.isMax == True:
            #Max heap
            if left < self.size and A[left] > A[heapIndex]:
                heapIndex = left #New largest
            if right < self.size and A[right] > A[heapIndex]:
                heapIndex = right #New largest
        else:
            #Min heap
            if left < self.size and A[left] < A[heapIndex]:
                heapIndex = left #New smallest
            if right < self.size and A[right] < A[heapIndex]:
                heapIndex = right #New smallest
        
        if heapIndex != i:
            A[i], A[heapIndex] = A[heapIndex], A[i] #Swap heap index with current iteration index
            self.heapify(A, heapIndex)

    def build_heap(self, A: list):
        """Build heap from given list"""
        self.size = len(A)
        med = (self.size // 2) - 1 #Mid point of array
        for i in range(0, med + 1): #Reverse iteration
            self.heapify(A, med - i) #Reverse iteration

class BinaryMinHeap(BinaryHeap):
    """Min binary heap implementation"""
    def __init__(self):
        self.isMax = False
        super()

class BinaryMaxHeap(BinaryHeap):
    """Max binary heap implementation"""
    def __init__(self):
        self.isMax = True
        super()

def heapsort(A: list, order: str = "asc") -> list:
    """Heapsort algorithm
    
    Parameters:
    ----------------
    a : list
        List of integers to order

    Returns:
    ----------------
    list
        Return ordered list
    """
    #Initialize heap based on order desired for array
    if order == "asc":
        auxHeap = BinaryMaxHeap()
    else:
        auxHeap = BinaryMinHeap()

    auxHeap.build_heap(A) #Build auxiliar heap

    for i in range(1, len(A) + 1): #Reverse iteration
        j = len(A) - i #Last index of heap
        A[0], A[j] = A[j], A[0] #Swap first with last
        auxHeap.size -= 1 #Decrease heap size
        auxHeap.heapify(A, 0) #Heapify

    return A
