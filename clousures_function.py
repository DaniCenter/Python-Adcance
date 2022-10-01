def make_division(number1: int):
    def division(number2: int):
        return number2 / number1
    return division
    # Esto es una funcion clousure


def run():
    entre_3 = make_division(3)
    res = entre_3(18)
    print(res)


if __name__ == "__main__":
    run()
