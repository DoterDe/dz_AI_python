def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль!"

def sum_of_two_numbers():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    return add(a, b)

print(f"Результат сложения: {sum_of_two_numbers()}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def get_factorial():
    number = int(input("Введите число для нахождения факториала: "))
    return factorial(number)

print(f"Факториал введённого числа: {get_factorial()}")


def check_even_odd():
    number = int(input("Введите число для проверки чётности: "))
    if number % 2 == 0:
        return "Число чётное"
    else:
        return "Число нечётное"

print(check_even_odd())



def find_max_of_three():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    return max(a, b, c)

print(f"Максимальное число: {find_max_of_three()}")


def fizz_buzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()


def reverse_words():
    sentence = input("Введите предложение: ")
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

print(reverse_words())


def reverse_string():
    string = input("Введите строку для переворота: ")
    return string[::-1]

print(reverse_string())



def multiplication_table():
    number = int(input("Введите число для таблицы умножения: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

multiplication_table()

