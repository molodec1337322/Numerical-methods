import math


def math_function(x):

    return 2 * x - math.log(10, x) - 7


def dihtomia(a, b, accuracy, math_function):

    iterations_count = 0

    X = (a + b) / 2
    current_accuracy = math.fabs(X)
    func_result_X = math_function(X)
    func_result_a = math_function(a)

    while current_accuracy >= accuracy:
        previous_result = X
        iterations_count += 1

        if func_result_X * func_result_a < 0:
            b = X
        else:
            a = X

        X = (a + b) / 2
        func_result_X = math_function(X)
        func_result_a = math_function(a)
        current_accuracy = math.fabs(X - previous_result)

    return X, iterations_count


def main():

    print("Введите левую границу: ")
    a = float(input())
    print("Введите правую границу: ")
    b = float(input())
    print("Введите необходимую точность")
    accuracy = float(input())

    result, iterations = dihtomia(a, b, accuracy, math_function)

    print("Ответ: ", result)
    print("Кол-во итреций: ", iterations)


if __name__ == "__main__":
    main()
