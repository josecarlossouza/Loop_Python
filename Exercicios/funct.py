# Faça uma função calculadora de dois números com três parâmetros: 
# os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. 
# Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.


def calculadora(num1, num2, op):
    if(op == "Soma"):
        return num1 + num2;
    elif(op == "Subtração"):
        return num1 - num2;
    elif(op == "Multiplicação"):
        return num1 * num2;
    elif(op == "Divisão"):
        return num1 / num2;
    else:
        return 0;

operacao = input("Informe qual operação de realizar - Soma, Subtração, Multiplicação ou Divisão: ");
um = float(input("Informe o primeiro número da operação: "));
dois = float(input("Informe o segundo número da operação: "));


print(f"\nO resultado da operação {operacao} dos números {um} e {dois} é: \n");

print(calculadora(um, dois, operacao));