import math


def math_function(x):

    return math.sin(math.log(math.exp(1), x))


def trapeze(start, end, step, math_func):

    iterations = 0
    sum = 0
    x = start

    while x <= end:
        iterations += 1
        sum += step * abs(math_func(x) + math_func(x + step)) / 2
        x += step

    return sum, iterations


def main():

    area, iterations = trapeze(2, 10, 0.0001, math_function)
    print("Площадь: ", area, " \nКол-во итраций: ", iterations)


if __name__ == "__main__":
    main()
