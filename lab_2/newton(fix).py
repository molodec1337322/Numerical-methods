import math


def kramer(x, y):

    main_determinant = math.sin(y + 0.5) * math.cos(x) - 2

    first_determinant = (math.cos(y + 0.5) + x - 0.8) * 2 - ((math.sin(x) - 2 * y - 1.6) * math.sin(y + 0.5))

    second_determinant = -(math.sin(x) - 2 * y - 1.6) + (math.cos(x) * (math.cos(y + 0.5) + x - 0.8))

    delta_x = first_determinant / main_determinant
    delta_y = second_determinant / main_determinant

    return delta_x, delta_y


def newton(accuracy):

    iterations = 0
    previous_x = 0
    previous_y = 0
    delta_x, delta_y = kramer(previous_x, previous_y)
    x = previous_x + delta_x
    y = previous_y + delta_y

    while accuracy < abs(delta_x) or accuracy < abs(delta_y):
        iterations += 1
        previous_x = x
        previous_y = y

        delta_x, delta_y = kramer(previous_x, previous_y)

        x = previous_x + delta_x
        y = previous_y + delta_y

    return x, y, iterations


def main():

    print("Введите точность: ")
    accuracy = float(input())

    x, y, it_count = newton(accuracy)

    print("x: ", x)
    print("y: ", y)
    print("Кол-во итераций: ", it_count)


if __name__ == '__main__':

    main()
