a = float(input("Ведіть число: "))
n = int(input("Введіть степінь: "))


def power(a, n):
        result = 1
        if n == 0:
                return result
        elif n > 0:
                for i in range(n):
                        result = result * a
        elif n < 0:
                for i in range(abs(n)):
                        result = result * (1/a)
        return result


print(power(a, n))


