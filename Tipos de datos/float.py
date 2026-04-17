# Tipo de dato que incluye a todos los enteros (integers) además de los racionales (fracciones)

# Por ejemplo:

num_float = 3.14159265359

# A diferencia de los enteros, en los float si está permitido colocar un 0 delante del número

float_sin_cero = 3.5
float_con_cero = 03.5

# ^^^ Ambos son válidos y significan lo mismo ^^^

# Tambien se puede usar el guión bajo (_) para separar los numeros para facilitar la lectura

# Por ejemplo:

float_sin_separar = 1454.792527
float_separado1 = 1_454.792_527
float_separado2 = 1454.79_25_27

# ^^^ Se puede poner el guión bajo en cualquier parte del número ^^^

# En un número decimal hay 2 partes, la parte entera (antes del punto) y la parte decimal (después del punto)
# Cualquiera de las dos partes puede estar vacía, pero no las dos al mismo tiempo

# Por ejemplo:

float_parte_decimal_vacia = 10.      # <--- Esto es lo mismo que escribir 10.0
float_parte_entera_vacia = .1      # <--- Esto es lo mismo que escribir 0.1