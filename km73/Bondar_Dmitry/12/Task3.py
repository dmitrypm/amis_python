numbers = input("Введіть послідовність натуральних чисел через пробіл: ").split()


def countm(list, ind = 0 , crt = 1, cmax = 1):
    if ind == len(list) - 1:
        return cmax
    elif list[ind] == list[ind + 1]:
        crt += 1
        if cmax < crt:
            cmax = crt
    else:
        crt = 1
    return countm(list, ind + 1, crt, cmax)


print(countm(numbers))
