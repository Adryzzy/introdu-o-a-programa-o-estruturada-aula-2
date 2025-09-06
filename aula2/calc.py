print("Atvidas do paulin")
print("me fale a Marca e o modelo do seu carro")
marca = input("Qual a Marca: ")
modelo = input("Qual o Modelo: ")
print("me fale quantos KM vc percorreu e quantos litros foram gastos")
km = float(input("me fale quantos km foram percorrido: "))
litros = float(input("me fale quantos litros foram gasto: "))


try:
    consumo = km / litros

    if consumo <= 6:
        qtc = "altissimo consumo"
    elif consumo <= 9:
        qtc = "alto consumo"
    elif consumo <= 12:
        qtc = "medio consumo"
    elif consumo <= 15:
        qtc = "bom consumo"
    elif consumo > 15:
        qtc = "otimo consumo"

except Exception as e:                                              
    print(f"O programa encontrou problemas, o erro foi {e}")


print(f"seu carro do modelo {modelo} da marca {marca} fez o consumo de {consumo} e isso é considerao um {qtc}")