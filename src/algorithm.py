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

def bubble_sort(heights_list):
    """bubble sort algorithm

    Args:
        heights_list (_type_): _description_

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_
    """
    for i in range(len(heights_list) - 1):
        for j in range(len(heights_list) - 1 - i):
            height01 = heights_list[j]
            height02 = heights_list[j + 1]

            if height01 > height02:
                heights_list = swap(heights_list, j, j + 1)
                yield True
    return heights_list