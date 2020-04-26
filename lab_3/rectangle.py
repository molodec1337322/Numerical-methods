import math


def math_function(x):

    return math.sin(math.log(math.exp(1), x))


def rectangle(start, end, step, math_func):

    iterations = 0
    sum = 0
    x = start

    while x <= end:
        iterations += 1
        sum += abs(math_func(x) * step)
        x += step

    return sum, iterations


def main():

    area, iterations = rectangle(2, 10, 0.0001, math_function)
    print("Площадь: ", area, " \nКол-во итраций: ", iterations)


if __name__ == "__main__":
    main()
