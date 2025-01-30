def multiplicadorProductosVendidos(productosVendidos):
    if productosVendidos > 20:
        return 13
    else:
        return 10

def calcularBonoVentas(productosVendidos):
    multiplicador = multiplicadorProductosVendidos(productosVendidos)
    return productosVendidos * multiplicador

# Ejemplos de uso
productosVendidos = 21
print(f"Multiplicador para {productosVendidos} productos vendidos: {multiplicadorProductosVendidos(productosVendidos)}")

productosVendidos = 7
print(f"Bono total para {productosVendidos} productos vendidos: {calcularBonoVentas(productosVendidos)}")

#Multiplicador para 21 productos vendidos: 13
#Bono total para 7 productos vendidos: 70
