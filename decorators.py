def mayuscula(func):
  def envoltura(texto):
    return func(texto).upper()
  return envoltura

@mayuscula # Esto equivaldria a hacer: mensaje = mayuscula(mensaje)
def mensaje(nombre):
  return f"{nombre}, recibiste un mensaje"

print(mensaje("danilo"))