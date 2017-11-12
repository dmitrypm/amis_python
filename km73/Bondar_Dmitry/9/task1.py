x1 = float(input("Введіть Х першої точки: "))
y1 = float(input("Введіть Y першої точки: "))
x2 = float(input("Введіть Х другої точки: "))
y2 = float(input("Введіть Y другої точки: "))


def distance(x1, y1, x2, y2):
    result = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    return result


print(distance(x1, y1, x2, y2))
