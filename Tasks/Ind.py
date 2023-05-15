from threading import Thread

EPSILON = 10 ** (-7)  # точность вычислений


def sum(x):
    n = 1
    sum = 1
    temp = x
    while abs(temp) >= EPSILON:
        sum += temp
        n += 1
        temp *= x

    print(f"Значение суммы для x={x}: {sum}")
    print(f"Проверка: 1/(1 - {x}) = {1 / (1 - x)}")


def main():
    x = 0.7

    # Создаем потоки
    thread1 = Thread(target=sum, args=(x,))
    thread2 = Thread(target=sum, args=(-x,))

    # Запускаем первый и второй поток
    thread1.start()
    thread2.start()

    # Ждем завершения выполнения первого и второго потока
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
