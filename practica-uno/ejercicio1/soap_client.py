from zeep import Client

client = Client('http://localhost:8000')

# Realizar operaciones
a = 10
b = 5

# Suma
result_suma = client.service.Operaciones(a=a, b=b, operacion="suma")
print(f"Suma de {a} y {b}: {result_suma['resultado']}")

# Resta
result_resta = client.service.Operaciones(a=a, b=b, operacion="resta")
print(f"Resta de {a} y {b}: {result_resta['resultado']}")

# Multiplicación
result_multiplicacion = client.service.Operaciones(a=a, b=b, operacion="multiplicacion")
print(f"Multiplicación de {a} y {b}: {result_multiplicacion['resultado']}")

# División
result_division = client.service.Operaciones(a=a, b=b, operacion="division")
print(f"División de {a} y {b}: {result_division['resultado']}")
