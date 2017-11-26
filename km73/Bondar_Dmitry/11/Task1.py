

def inputs(list = []):
    a = input("Введіть елемент\nEnter для продовження\n")
    if a == "":
        return list
    else:
        list.append(a)
        return inputs(list)


def func(listA, ind = -1, listB = []):
    if ind >= len(listA) - 1:
        return listB
    else:
        listB.append(listA[ind])
        return func(listA, ind + 1, listB)
    

print(func(inputs()))
