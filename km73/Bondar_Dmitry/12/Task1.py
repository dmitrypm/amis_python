numbers = input("Введіть послідовність натуральних чисел через пробіл: ").split()


def second_max(list, min = 0, max = 1, ind = 2):
    """

    Arguments:
        list
    
    Returns:
        Second maximum of the list

    """
    

    if len(list) == 2:
        return (list[min] if float(list[min]) <= float(list[max]) else list[max])
    if ind == len(list):
        return list[min]
    elif float(list[max]) >= float(list[ind]):
        return (second_max(list, min, max, ind + 1) if float(list[min]) >= float(list[ind]) else second_max(list, ind, max, ind + 1))
    else:
        return (second_max(list, min, ind, ind + 1) if float(list[min]) >= float(list[max]) else second_max(list, max, ind, ind + 1))


print(second_max(numbers))
                
