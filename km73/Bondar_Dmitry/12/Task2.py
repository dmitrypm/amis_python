numbers = input("Введіть послідовність натуральних чисел через пробіл: ").split()


def count_max(list, max = 0, ind = 1, count = 0):
    """

    Arguments:
        list
    
    Returns:
        Count maximum elements of the list

    """
    
    if ind == len(list):
        for i in range(len(list)):
            if list[i] == list[max]:
                count +=1
        return count
    elif float(list[max]) >= float(list[ind]):
        return count_max(list, max, ind + 1)
    else:
        return count_max(list, ind, ind + 1)

    
print(count_max(numbers))
