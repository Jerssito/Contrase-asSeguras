Explicación:
Módulo secrets: Se usa para generar números aleatorios criptográficamente seguros. Esto es preferible sobre random cuando se trata de generar contraseñas o cualquier cosa relacionada con la seguridad.
Módulo string: Proporciona constantes como ascii_letters (letras mayúsculas y minúsculas), digits (dígitos del 0 al 9) y punctuation (caracteres especiales).
Función generar_contrasena: Recibe dos parámetros:
longitud: Longitud de la contraseña (por defecto es 12).
incluir_simbolos: Indica si se deben incluir caracteres especiales (por defecto es True).
Este generador garantiza que la contraseña sea segura mediante el uso de aleatoriedad criptográfica y caracteres variados.