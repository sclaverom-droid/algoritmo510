def clasificar_imc(peso, altura):
    # Calculamos el IMC
    imc = peso / (altura ** 2)
    
    # Clasificamos según el valor obtenido
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Normal"
    else:
        categoria = "Sobrepeso"
        
    return categoria

# --- Ejemplo de uso para probarlo ---
peso_ejemplo = 70      # en kilogramos
altura_ejemplo = 1.75  # en metros

resultado = clasificar_imc(peso_ejemplo, altura_ejemplo)
print(f"El paciente tiene un peso: {resultado}")