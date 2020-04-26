import math


def math_function(x):

    return math.sin(math.log(x))


def trapeze(start, end, step, math_func):

    iterations = 0
    sum = 0
    x = start

    while x + step < end:
        iterations += 1
        sum += step * abs(math_func(x) + math_func(x + step)) / 2
        x += step

    return sum, iterations


def main():

    true_area = 7.19118686078937
    area, iterations = trapeze(2, 10, 0.001, math_function)
    print("Площадь: ", area, " \nКол-во итраций: ", iterations)
    print("Отклонение: ", abs(true_area - area))


if __name__ == "__main__":
    main()
