variable = None
localVariable = None


def run():
    localVariable = "Sin valor"
    print(variable)
    print(localVariable)

    def cambiar():
        global variable
        nonlocal localVariable
        # nonlocal sirve para acceder a una variable local
        # global sirve para acceder a una variable global
        variable = "Cambie de valor"
        localVariable = "Cambie de valor local"
    cambiar()
    print(variable)
    print(localVariable)


if __name__ == "__main__":
    run()
