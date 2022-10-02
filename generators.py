import time

# Los generadores funcionan igual que los iteradores, pero mas bonitos ;D


def fibonacciGen(max=None):
    n = 2
    count = 0

    if max:
        while count < max:
            temp = [i for i in range(2, n) if n % i == 0]
            aux = n
            if not temp:
                count += 1
                yield aux
    else:
        while True:
            temp = [i for i in range(2, n) if n % i == 0]
            aux = n
            n += 1
            if not temp:
                yield aux


if __name__ == "__main__":
    res = fibonacciGen(5)
    for i in res:
        print(i)
        time.sleep(0.5)
