def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1  # Move right if the right element is greater
        else:
            high = mid  # Move left otherwise, including when equal

    return list_of_integers[low] if list_of_integers else None
