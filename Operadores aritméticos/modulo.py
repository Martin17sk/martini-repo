# El operador módulo (%) conocer el resto de una división
# Tambien se puede interpretar como: 
# "Cuanto falta para llegar al primer número desde el múltiplo del segundo número más alto sin pasar al primero número"

# Por ejemplo:

5 % 2

# "(...) desde el múltiplo del segundo número más alto sin pasar al primero número"
# Múltiplo de 2 más alto sin pasar al 5

# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6     <--- Aqui ya nos pasamos del 5, es decir, el múltiplo de 2 más alto sin pasar al 5 es 4

# "Cuanto falta para llegar al primer número (...)"

# Desde el 4 falta 1 para llegar a 5, entonces el resultado de 5 módulo 2 es 1 (5 % 2 = 1)

# El módulo sirve típicamente para saber si un número es par o impar

x = 4

if x % 2 == 0:
    print(f"El {x} es par")
else:
    print(f"El {x} es impar")

# Operador compuesto

y = 10
y %= 3          # 1         (y = y % 3)