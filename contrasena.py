import string

# Autor: Jersson Morocho
# Este script genera una contraseña estática tomando caracteres de un conjunto predefinido
# La contraseña generada no es aleatoria, sino que se seleccionan caracteres fijos
# del conjunto de caracteres posibles en posiciones determinadas.

# Definir los caracteres posibles:
# Usamos las letras mayúsculas, minúsculas, los números y los símbolos
letras_mayusculas = string.ascii_uppercase  # A-Z (mayúsculas)
letras_minusculas = string.ascii_lowercase  # a-z (minúsculas)
numeros = string.digits                    # 0-9 (números)
simbolos = string.punctuation               # ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~ (símbolos)

# Unir todos los conjuntos de caracteres en uno solo
# Concatenamos todos los conjuntos de caracteres posibles en una sola cadena
todos_los_caracteres = letras_mayusculas + letras_minusculas + numeros + simbolos

# Generar una contraseña de manera fija (sin aleatoriedad):
# En lugar de generar caracteres aleatorios, seleccionamos caracteres en posiciones fijas
# de la cadena `todos_los_caracteres`. Este enfoque no tiene aleatoriedad, por lo que la contraseña
# será siempre la misma si no cambiamos los índices.

# Selección de caracteres con índices fijos de la cadena `todos_los_caracteres`:
contrasena = todos_los_caracteres[0] + todos_los_caracteres[5] + todos_los_caracteres[10] + \
             todos_los_caracteres[15] + todos_los_caracteres[20] + todos_los_caracteres[25] + \
             todos_los_caracteres[30] + todos_los_caracteres[35] + todos_los_caracteres[40] + \
             todos_los_caracteres[45] + todos_los_caracteres[50] + todos_los_caracteres[55]

# Mostrar la contraseña generada:
# Finalmente, mostramos la contraseña generada en la consola.
# Como no hay aleatoriedad, esta contraseña será siempre la misma.
print("Contraseña generada:", contrasena)
