numbers = input("Введіть послідовність натуральних чисел через пробіл: ").split()


def smax(list, mid = 0, max = 1, ind = 2):
    if len(list) == 2:
        return (list[mid] if float(list[mid]) <= float(list[max]) else list[max])
    if ind == len(list):
        return list[mid]
    elif float(list[max]) >= float(list[ind]):
        return (smax(list, mid, max, ind + 1) if float(list[mid]) >= float(list[ind]) else smax(list, ind, max, ind + 1))
    else:
        return (smax(list, mid, ind, ind + 1) if float(list[mid]) >= float(list[max]) else smax(list, max, ind, ind + 1))


print(smax(numbers))
                
