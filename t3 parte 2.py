def multiplicadorDiasFaltandes(diasFaltantes):
    if diasFaltantes >= 5:
        return 0.85
    else:
        return 1

def multiplicadorProductosVendidos(productosVendidos):
    if productosVendidos > 20:
        return 13
    else:
        return 10

def calcularBonoVentas(productosVendidos):
    multiplicador = multiplicadorProductosVendidos(productosVendidos)
    return productosVendidos * multiplicador

def calcularSalarioFinal(diasFaltantes, productosVendidos, salario_base=1000):
    # Aplicar la penalización al salario base
    salario_con_penalizacion = salario_base * multiplicadorDiasFaltandes(diasFaltantes)
    
    # Calcular el bono por ventas
    bono_ventas = calcularBonoVentas(productosVendidos)
    
    # Calcular el salario final
    salario_final = salario_con_penalizacion + bono_ventas
    
    # Asegurarse de que el salario final no sea mayor a 2000.00
    if salario_final > 2000:
        salario_final = 2000
    
    return salario_final

# Ejemplo de uso
diasFaltantes = 2
productosVendidos = 3
print(f"Salario final: {calcularSalarioFinal(diasFaltantes, productosVendidos)}")


#Salario final: 1030

