# Ejemplos de manejo de cadenas y variables en Python

# Definición de variables
nombre = "Juan"
edad = 25
saldo = 1000.50
profesion = "Ingeniero"

# Concatenación de cadenas
saludo = "¡Hola, " + nombre + "!"
print(saludo)

# Cadena con salto de línea y tabulación
cadena_multilinea = "Línea 1\nLínea 2\nLínea 3\t\tLínea 4\nLínea 5"
print(cadena_multilinea)

# Cadena con formato usando tabulación
informacion = f"Nombre:\t\t{nombre}\nEdad:\t\t{edad}\nProfesión:\t{profesion}"
print(informacion)
# impresion de 

# Operaciones con cadenas
cadena = "Python es un lenguaje de programación"
longitud = len(cadena)
print("Longitud de la cadena:", longitud)

# Reemplazo de caracteres o subcadenas
nueva_cadena = cadena.replace("lenguaje", "framework")
print("Cadena con reemplazo:", nueva_cadena)
