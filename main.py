def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

number = int(input("Введіть число: "))
print(f"Факторіал числа {number} дорівнює {factorial(number)}")
