# ----- FOR -----
# La estrucutra de control "for" sirve para ejecutar
# un mismo bloque de código una cantidad determinada de veces.

# A diferencia del "while", el "for" requiere una cantidad exacta de veces en la que se repetirá,
# esa es su gracia, ya que de necesitar repetir un bloque de código una cantidad de veces indeterminada,
# se usaría el "while".

# -------------------------------------------------

# El "for" en python tiene varias utilidades:

# 1. Iterar una cantidad N de veces (Siendo N un número entero positivo)

# ¡IMPORTANTE!
# El método "range()" puede recibir de 1 hasta 3 argumentos (Lo que va dentro del paréntesis) numéricos

# - Un argumento:
# Comenzando desde 0 hasta el número indicado -1
# (Siendo X el argumento: Desde 0 hasta X-1, de 1 en 1)

for i in range(5):
    print(i)                # 0 1 2 3 4

# - Dos argumentos:
# Comenzando desde el primer número indicado hasta el segundo número indicado -1
# (Siendo X e Y los argumentos resepectivos: Desde X hasta Y-1, de 1 en 1)

for i in range(1,3):
    print(i)                # 1 2

# - Tres argumentos:
# Comenzando desde el primer número indicado hasta el segundo número indicado, con paso el tercer número indicado
# (Siendo X, Y y Z los argumentos respectivos: Desde X hasta Y-1, de Z en Z)

for i in range(4,12,2):
    print(i)                # 4 6 8 10

# -------------------------------------------------

# 2. Iterar sobre un string
# Recorre cada CARACTER del string (incluye letras, símbolos y números)

for letra in "Buenos días":
    print(letra)            # B u e n o s   d í a s

# -------------------------------------------------

# 3. Iterar en listas

for i in [1,5,3,89,15]:
    print(i)                # 1 5 3 89 15

# -------------------------------------------------

# For...else
# El "for", al igual que el "if", tiene un "else" el cual se ejecuta siempre y cuando no haya habido un "break"

# Por ejemplo:
print(50*"-")

for i in range(5):
    print(i)                    # 0 1 2 3
    if i == 3:
        break
else:
    print("For completado")     # NO alcanza a ejecutarse

print(50*"-")

for i in range(5):
    print(i)                    # 0 1 2 3 4
else:
    print("For completado")     # Si se ejecuta

print(50*"-")

# -------------------------------------------------

# reversed()
# A cualquier (creo) cosa despues del "in" se le puede agregar un "reversed(aqui dentro va la cosa)" para recorrer de forma invertida

# Por ejemplo:
for i in reversed(range(5)):
    print(i)                        # 4 3 2 1 0

print(50*"-")

for i in reversed([2,4,6,8,10]):
    print(i)                        # 10 8 6 4 2

print(50*"-")

for letra in reversed("Hola"):
    print(letra)                    # a l o H