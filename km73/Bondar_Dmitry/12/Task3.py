numbers = input("Введіть послідовність натуральних чисел через пробіл: ").split()


def largest_group(list, ind = 0 , group = 1, max_group = 1):
    """

    Arguments:
        list
    
    Returns:
        The largest group

    Example:
        >>>[1, 2, 2, 2, 3, 3,]
        3

    """
    if ind == len(list) - 1:
        return max_group
    elif list[ind] == list[ind + 1]:
        group += 1
        if max_group < group:
            max_group = group
    else:
        group = 1
    return largest_group(list, ind + 1, group, max_group)


print(largest_group(numbers))
