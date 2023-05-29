import re

def validar_nombre(palabra):
    patron = r'^[a-zA-Z\s]+$'
    match = re.search(patron, palabra)
    if match:
        palabra = match.group()
        if " " in palabra:
            # Si la palabra tiene un espacio, capitalizar ambas palabras
            palabras = palabra.split()
            palabras_capitalizadas = []
            for p in palabras:
                palabras_capitalizadas.append(p.capitalize())
                palabra_validada = " ".join(palabras_capitalizadas)
        else:
            # Si la palabra no tiene un espacio, capitalizarla
            palabra_validada = palabra.capitalize()
        return palabra_validada
    else:
        return None

# print(validar_nombre("jose sntonio"))

def validar_numero(numero):
    cadena = str(numero)    # Convertir a cadena si es necesario
    patron = r'^\d+$'       # Patrón para validar solo dígitos
    if re.match(patron, cadena):
        return True
    else:
        return False


# print(validar_numero(2))


