def multiplicadorDiasFaltandes(diasFaltantes):
    if diasFaltantes >= 5:
        return 0.85
    else:
        return 1

# Ejemplos de uso
diasFaltantes = 3
print(f"Multiplicador para {diasFaltantes} días faltantes: {multiplicadorDiasFaltandes(diasFaltantes)}")

diasFaltantes = 7
print(f"Multiplicador para {diasFaltantes} días faltantes: {multiplicadorDiasFaltandes(diasFaltantes)}")



#Multiplicador para 3 días faltantes: 1
#Multiplicador para 7 días faltantes: 0.85