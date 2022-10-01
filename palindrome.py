def is_prime(number: int) -> bool:
    results_list = [x for x in range(2, number) if number % x == 0]
    return len(results_list) == 0


def run():
    print(is_prime(4))
    # Para poder verificar que recivimos los tipos indicados usamos:
    # mypy .\palindrome.py --check-untyped-defs
    # tener instalado el modulo mypy


if __name__ == "__main__":
    run()
