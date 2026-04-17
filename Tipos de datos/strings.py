# Tipo de dato que incluye todos los caracteres del teclado, es decir, numeros, letras, símbolos y vacío
# Se pueden escribir entre comillas simples (') o comillas dobles (")
# Nota 1: El espacio se considera un caracter
# Nota 2: Con la comilla que inicie debe ser la misma con la que termina

# Por ejemplo:

vacio1 = ""
vacio2 = ''

numero1 = "1234"
numero2 = '1234'

letra1 = "aAbBcC"
letra2 = 'aAbBcC'

simbolo1 = "@#$%& /()[]+*"
simbolo2 = '@#$%& /()[]+*'

# Un string puede contener dentro la otra comilla que no se usó para iniciar el string

# Por ejemplo:

comilla_simple_con_doble = 'Mis últimas palabras van a ser "Adiós Mundo", que chistoso'
comilla_doble_con_simple = "Digan 'Buenos días' cuando se suban a la micro"

# ¿Y si quiero utilizar la misma comilla con la que inicie el string, pero dentro del string?
# Si se puede pero tiene un pequeño truco, antes de donde iría la comilla hay que colocar un backslash (\)
# Nota: No confundir con el slash (/)
# Para escribir el slash, por lo general, es con la combinacion SHIFT + 7 (/)
# Para escribir el backslash, por lo general, es con la combinacion AltGr + ' (\) (AltGr + "La tecla al lado derecho del 0")

# Por ejemplo:

comilla_simple_con_simple = 'Pepito le dijo \'Hola\' y se fué'
comilla_doble_con_doble = "Juanita le respondió \"Tonto\", y tambien se fué"

print("-----\n")
print(comilla_simple_con_simple)
print(comilla_doble_con_doble)
print("\n-----")

# Existe la triple comilla (simple o doble), una función que tiene es la de poder seguir escribiendo en la siguiente línea

# Por ejemplo:

triple_comilla = """Este texto es tan pero tan largo
que tengo seguir en la siguiente línea"""

print(triple_comilla)

print(50*"-")

# Existen distintas funciones con el backslash (\), algunas de ellas son:

# 1. Backslash (\): Permite saltar una línea en el editor, sin embargo, al ejecutar el salto de línea no se ejecuta

backslash = "En este texto " \
"voy a usar un backslash"

print(backslash)
print(50*"-")

# 2. Doble backslash (\\): Permite escribir el simbolo del backslash dentro del string

string_con_backslash = "Este string tiene un \\ dentro"

print(string_con_backslash)
print(50*"-")

# 3. Backslash + comilla (\' o \"): Permite escribir el simbolo de la comilla dentro del string

string_con_comilla = "Tengo que escribier un texto que use \' y \", oh ya lo hice"

print(string_con_comilla)
print(50*"-")

# 4. Backslash + n (\n): Permite hacer un salto de línea dentro del string

string_con_salto_de_linea = "Esta es la línea 1\nEsta es la línea 2"

print(string_con_salto_de_linea)
print(50*"-")

# 5. Backslash + t (\t): Permite hacer una tabulación

string_con_tabulacion = "Aqui no hay tabulación\n\tAqui si hay tabulación"

print(string_con_tabulacion)
print(50*"-")