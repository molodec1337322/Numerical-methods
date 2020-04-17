import math


def math_function(x):

    return 2 * x + math.log(10, x) - 7


def first_derivative(x):

    return 2 - 1 / (x * math.log(math.exp(1), 10))


def second_derivative(x):

    return 1 / (x * x * math.log(math.exp(1), 10))


def newton(a, b, accuracy, math_function, first_derivative, second_derivative):

    iterations_count = 0
    current_accuracy = math.fabs(a - b)

    if math_function(a) * second_derivative(a) < 0:
        X = a
    else:
        X = b

    while current_accuracy >= accuracy:
        iterations_count += 1
        print(iterations_count, "  ", X)
        previous_result = X
        X = X - (math_function(X) / first_derivative(X))
        current_accuracy = math.fabs(X - previous_result)

    return X, iterations_count


def main():

    print("Введите левую границу: ")
    a = float(input())
    print("Введите правую границу: ")
    b = float(input())
    print("Введите необходимую точность")
    accuracy = float(input())

    result, iterations = newton(a, b, accuracy, math_function, first_derivative, second_derivative)

    print("Ответ: ", result)
    print("Кол-во итреций: ", iterations)


if __name__ == "__main__":
    main()
