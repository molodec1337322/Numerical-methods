import math


def jacobi(accuracy):

    iterations = 0
    previous_x = 0
    previous_y = 0

    x = -math.cos(previous_y + 0.5) + 0.8
    y = (math.sin(previous_x) - 1.6) / 2

    epsilon = max(abs(x - previous_x), abs(y - previous_y))

    while accuracy < epsilon:

        iterations += 1
        previous_x = x
        previous_y = y

        x = -math.cos(previous_y + 0.5) + 0.8
        y = (math.sin(previous_x) - 1.6) / 2

        epsilon = max(abs(x - previous_x), abs(y - previous_y))

    return x, y, iterations


def main():

    print("Введите точность: ")
    accuracy = float(input())

    x, y, it_count = jacobi(accuracy)

    print("x: ", x)
    print("y: ", y)
    print("Кол-во итераций: ", it_count)


if __name__ == '__main__':

    main()
