numbers = input("Введіть послідовність натуральних чисел через пробіл: ").split()


def cmax(list, max = 0, ind = 1, count = 0):
    if ind == len(list):
        for i in range(len(list)):
            if list[i] == list[max]:
                count +=1
        return count
    elif float(list[max]) >= float(list[ind]):
        return cmax(list, max, ind + 1)
    else:
        return cmax(list, ind, ind + 1)

    
print(cmax(numbers))
