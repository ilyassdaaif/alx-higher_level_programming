#!/usr/bin/python3
"""script for finding peak in list of ints, interview prep
"""

"""
    THOUGHT PROCESS
        it is not sorted, so sorting would take n(log(n))
            -> not worth sorting
        looping through and keeping track of max (brute force)
            -> O(n)

        possibly looping from each end reducing to 1/2 run time
            -> still O(n)
        
        best solution: Use a modified binary search to find a peak in O(log n) time.
"""

def find_peak(list_of_integers):
    """Binary search implementation to find a peak efficiently.
    """
    if not list_of_integers:
        return None
    
    low, high = 0, len(list_of_integers) - 1
    
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1  # The peak must be in the right half if the right neighbor is greater
        else:
            high = mid  # The peak is in the left half or at mid

    return list_of_integers[low]  # low and high converge to the index of a peak
