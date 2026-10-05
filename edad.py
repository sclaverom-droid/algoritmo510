def Acceso_voto(edad):
    edad_mínima = edad >= 18
    return edad_mínima
print(Acceso_voto(20))  # Devuelve: True
print(Acceso_voto(15))  # Devuelve: False