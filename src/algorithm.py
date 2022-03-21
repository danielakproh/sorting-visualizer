def swap(heights_list, index01, index02):
    """swap two positions in a list at given indexes 

    Args:
        heights_list (list): iterable in which swapping occurs
        index01 (int): index of first element
        index02 (int): index of second element

    Returns:
        list: list with element positions swapped
    """
    heights_list[index01], heights_list[index02] = heights_list[index02], heights_list[index01]
    return heights_list

def bubble_sort(_list):
    """bubble sort algorithm

    Args:
        _list (list): list to sort

    Returns:
        list: bubbly sorted list

    Yields:
        bool: True
    """
    for i in range(len(_list) - 1):
        for j in range(len(_list) - 1 - i):
            height01 = _list[j]
            height02 = _list[j + 1]

            if height01 > height02:
                _list = swap(_list, j, j + 1)
                yield True
    return _list