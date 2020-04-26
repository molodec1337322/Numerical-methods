import math


def math_function(x):

    return math.sin(math.log(x))


def rectangle(start, end, step, math_func):

    iterations = 0
    sum = 0
    x = start

    while x + step < end:
        iterations += 1
        sum += abs(math_func(x) * step)
        x += step

    return sum, iterations


def main():

    true_area = 7.19118686078937
    area, iterations = rectangle(2, 10, 0.001, math_function)
    print("Площадь: ", area, " \nКол-во итраций: ", iterations)
    print("Отклонение: ", abs(true_area - area))

    
if __name__ == "__main__":
    main()
