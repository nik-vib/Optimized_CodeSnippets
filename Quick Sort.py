def quicksort(arr):
    """
    Optimized implementation of QuickSort algorithm.
    
    Optimizations:
    - Median-of-three pivot selection
    - Insertion sort for small subarrays
    - Tail-call optimization for the larger partition
    - Three-way partitioning for handling duplicates efficiently
    """
    def insertion_sort(arr, low, high):
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i - 1
            while j >= low and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    
    def median_of_three(arr, low, high):
        mid = (low + high) // 2
        # Sort low, mid, high values
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        # Place pivot at high-1
        arr[mid], arr[high-1] = arr[high-1], arr[mid]
        return arr[high-1]
    
    def three_way_partition(arr, low, high, pivot):
        """
        Partition array into three parts:
        - Elements smaller than pivot
        - Elements equal to pivot
        - Elements greater than pivot
        """
        i = low      # Iterator
        lt = low     # Elements < pivot
        gt = high    # Elements > pivot
        
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        
        return lt, gt
    
    def _quicksort(arr, low, high):
        while high - low > 10:  # Use insertion sort for small arrays
            # Choose pivot using median-of-three
            pivot = median_of_three(arr, low, high)
            
            # Three-way partition
            left, right = three_way_partition(arr, low, high, pivot)
            
            # Tail-call optimization: recursively sort smaller partition
            if left - low < high - right:
                _quicksort(arr, low, left - 1)
                low = right + 1
            else:
                _quicksort(arr, right + 1, high)
                high = left - 1
        
        if high - low > 0:
            insertion_sort(arr, low, high)
    
    if len(arr) <= 1:
        return arr
    
    _quicksort(arr, 0, len(arr) - 1)
    return arr
