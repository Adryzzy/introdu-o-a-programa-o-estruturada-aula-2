print("Verificador se é maior de idade de acordo com a idade")
n2 = input("Qual seu nome? ")
n1 = int(input("fale sua idade? "))


if n1 > 18:
    print(f"{n2} você maior de idade")

elif n1 == 18:
    print(f"{n2} você é maior de idade, com 18 anos completos.")

elif n1 < 18:
    print(f"{n2} você é menor de idade")


n3 = float(input("insira seu peso em KG: "))
n4 = float(input("insira sua altura em Metros: "))

try:
    imc = n3 / (n4*n4)
        
    if imc <= 18.5:
        print(f"{n2} seu IMC é de: {imc} portanto, você está abaixo do peso")
    elif imc <= 24.9:
        print(f"{n2} seu IMC é de: {imc} portanto, você está dentro do peso ideal")
    elif imc <= 29.9:
        print(f"{n2} seu IMC é de: {imc} portanto, você está com sobrepeso")
    elif imc > 29.9:
        print(f"{n2} seu IMC é de: {imc} portanto, você está com obesidade")


except Exception as e:                                               ### Escolha um dos primeiros except para roda
    print(f"O programa encontrou problemas, o erro foi {e}")

    """
    except ZeroDivisionError:                                                   
    print("O programa não é capaz de dividir por Zero!")
    """