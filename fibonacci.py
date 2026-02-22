def fibonacci(n):
    """Генерирует первые n чисел Фибоначчи"""
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


if __name__ == "__main__":
    # Пример использования
    result = fibonacci(10)
    print("Первые 10 чисел Фибоначчи:", result)
    
    # Генерируем 15 чисел
    result_15 = fibonacci(15)
    print("Первые 15 чисел Фибоначчи:", result_15)
