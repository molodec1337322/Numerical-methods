import math


def math_function(x):

	return 2 * x - math.log10(x) - 7


def cords(a, b, accuracy, math_function):

	iterations_count = 0
	current_accuracy = math.fabs(a - b)
	X = a

	while current_accuracy >= accuracy:
		iterations_count += 1
		previous_X = X
		X = X - ((b - X)/(math_function(b) - math_function(X))) * math_function(X)
		if math_function(X) * math_function(b) >= 0:
			b = X
		current_accuracy = math.fabs(previous_X - X)

	return X, iterations_count


def main():

	print("Введите левую границу: ")
	a = float(input())
	print("Введите правую границу: ")
	b = float(input())
	print("Введите необходимую точность")
	accuracy = float(input())

	result, iterations = cords(a, b, accuracy, math_function)

	print("Ответ: ", result)
	print("Кол-во итреций: ", iterations)


if __name__ == "__main__":
	main()
