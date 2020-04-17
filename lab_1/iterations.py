import math


def math_function(x):

	return 2 * x - math.log10(x) - 7


def x_function(x):

	return (math.log10(x) + 7) / 2


def newton(a, b, accuracy, math_function, x_function):

	iterations_count = 0
	current_accuracy = math.fabs(a - b)
	X = (b - a) / 2
	X = x_function(X)

	while current_accuracy >= accuracy:
		previous_result = X
		X = x_function(X)
		current_accuracy = math.fabs(X - previous_result)

	return X, iterations_count


def main():

	print("Введите левую границу: ")
	a = float(input())
	print("Введите правую границу: ")
	b = float(input())
	print("Введите необходимую точность")
	accuracy = float(input())

	result, iterations = newton(a, b, accuracy, math_function, x_function)

	print("Ответ: ", result)
	print("Кол-во итреций: ", iterations)


if __name__ == "__main__":
	main()
