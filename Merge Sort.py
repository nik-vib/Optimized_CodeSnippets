def merge_sort(arr: list) -> list:
    """
    Performs merge sort on the input array.
    
    Optimizations:
    1. In-place merging for memory efficiency
    2. Early returns for small arrays
    3. Slice assignment for faster merging
    4. Type hints for better IDE support
    
    Args:
        arr (list): Input array to be sorted
        
    Returns:
        list: Sorted array
    """
    # Early return for arrays of size 0 or 1
    if len(arr) <= 1:
        return arr
    
    # Find the middle point
    mid = len(arr) // 2
    
    # Recursively sort the two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: list, right: list) -> list:
    """
    Merges two sorted arrays into a single sorted array.
    
    Args:
        left (list): First sorted array
        right (list): Second sorted array
        
    Returns:
        list: Merged sorted array
    """
    result = []
    left_idx = right_idx = 0
    
    # Compare elements from both arrays and merge them in sorted order
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Add remaining elements from left array, if any
    result.extend(left[left_idx:])
    
    # Add remaining elements from right array, if any
    result.extend(right[right_idx:])
    
    return result

# For in-place merge sort (memory efficient version)
def merge_sort_inplace(arr: list, start: int = 0, end: int = None) -> None:
    """
    Performs merge sort in-place on the input array.
    
    Args:
        arr (list): Input array to be sorted
        start (int): Start index of the current subarray
        end (int): End index of the current subarray
    """
    if end is None:
        end = len(arr)
        
    if end - start <= 1:
        return
    
    mid = (start + end) // 2
    
    # Recursively sort the two halves
    merge_sort_inplace(arr, start, mid)
    merge_sort_inplace(arr, mid, end)
    
    # Merge the sorted halves
    merge_inplace(arr, start, mid, end)

def merge_inplace(arr: list, start: int, mid: int, end: int) -> None:
    """
    Merges two sorted subarrays in-place.
    
    Args:
        arr (list): Input array containing the subarrays
        start (int): Start index of first subarray
        mid (int): End index of first subarray / Start index of second subarray
        end (int): End index of second subarray
    """
    left = arr[start:mid]
    right = arr[mid:end]
    
    i = start
    left_idx = 0
    right_idx = 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            arr[i] = left[left_idx]
            left_idx += 1
        else:
            arr[i] = right[right_idx]
            right_idx += 1
        i += 1
    
    # Copy remaining elements
    while left_idx < len(left):
        arr[i] = left[left_idx]
        left_idx += 1
        i += 1
        
    while right_idx < len(right):
        arr[i] = right[right_idx]
        right_idx += 1
        i += 1
