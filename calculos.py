def calcular(num1, num2, calculo):
    if (calculo == "soma"):
        soma = int(num1) + int(num2)
        return {
            "Resultado": str(soma)
        }

    elif (calculo == "subtracao"):
        subtracao = int(num1) - int(num2)
        return {
            "Resultado": str(subtracao) 
        }
    elif (calculo == "multiplicacao"):
        multiplicacao = int(num1) * int(num2)
        return {
            "Resultado": str(multiplicacao) 
        }
    elif (calculo == "juros"):
        juros1 = int(num2) / 100
        juros2 = int(num1) * juros1
        juros3 = int(num1) + juros2
        return {
            "Resultado": str(juros3) 
        }   
    else:
        divisao = int(num1) // int(num2)
        return {
            "Resultado": str(divisao) 
        }
