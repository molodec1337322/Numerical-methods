import math


def math_function(x):

    return math.sin(math.log(x))


def simpson(start, end, step, math_func):

    iterations = 0
    sum = 0
    x = start

    while x + step < end:
        iterations += 1
        sum += (step / 3) * abs(math_func(x - step) + 4 * math_func(x) + math_func(x + step))
        x += 2 * step

    return sum, iterations


def main():

    true_area = 7.19118686078937
    area, iterations = simpson(2, 10, 0.001, math_function)
    print("Площадь: ", area, " \nКол-во итраций: ", iterations)
    print("Отклонение: ", abs(true_area - area))


if __name__ == "__main__":
    main()
