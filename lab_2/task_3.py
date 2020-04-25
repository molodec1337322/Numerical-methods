import math


def compute(equation_lines):
    
    k = 8

    x = [0] * equation_lines
    u = [0] * equation_lines
    v = [0] * equation_lines

    a = [0] * equation_lines
    b = [0] * equation_lines
    c = [0] * equation_lines
    d = [0] * equation_lines

    b[1] = -1
    c[1] = pow(5, 7)
    d[1] = 5
    u[1] = - c[1] / b[1]
    v[1] = d[1] / b[1]

    for i in range(2, equation_lines):

        a[i] = i + k

        b[i] = math.pow(-1, i + k)
        c[i] = math.pow(-i + k, i + k)
        d[i] = k - i

        u[i] = - c[i] / (a[i] * u[i - 1] + b[i])
        v[i] = (d[i] - a[i] * v[i-1]) / (a[i] * v[i - 1] + b[i])

    x[equation_lines - 1] = (d[equation_lines - 1] - a[equation_lines - 1] * v[equation_lines - 1 - 1]) / (a[equation_lines - 1] * u[equation_lines - 1 - 1] + b[equation_lines - 1])

    for i in range(equation_lines - 2, 0, -1):
        x[i] = u[i] * x[i + 1] + v[i]

    return x


def main():

    print("Введите количество строк: ")
    n = int(input())
    n += 1

    c = []

    if n > 1:
        c = compute(n)
    else:
        c[0] = -7

    for i in range(1, n):
        print(c[i])


if __name__ == "__main__":

    main()
