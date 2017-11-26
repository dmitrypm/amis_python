

def inputs(list = []):
    a = input("Введіть елемент\nEnter для продовження\n")
    if a == "":
        return list
    else:
        list.append(a)
        return inputs(list)


 
def mins(list, minind = 0, ind = 1):
    if ind == len(list):
        return list[minind]
    elif float(list[minind]) <= float(list[ind]):
        return mins(list, minind, ind + 1)
    else:
        return mins(list, ind, ind + 1)


print(mins(inputs()))
