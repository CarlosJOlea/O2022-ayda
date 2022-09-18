
# Nombre: Carlos Jesus Olea Diaz 
# No. Control: 18012182
# Calificación: XXX

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


numero = int(input("Ingresa el numero factorial: "))
print(factorial(numero))
