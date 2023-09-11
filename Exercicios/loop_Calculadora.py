# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
# No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
# o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. 
# Depois precisa executar a operação e mostrar o resultado na tela. 
# Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 



#importa a função sleep, para adicionar pequenas pausas no código
from time import sleep

#função que irá calcular o valor da operação de dois números de acordo com a operação (op)
def calculadora(num1, num2, op):
    if(op == 1):
        return num1 + num2;
    elif(op == 2):
        return num1 - num2;
    elif(op == 3):
        return num1 * num2;
    elif(op == 4):
        return num1 / num2;
    else:
        return 0;

#loop para manter o programa funcionando até o usuário digitar "0"
while True:
    print("\nInforme o número correspondente a operação que deseja realizar ou 0 para sair:");
    print("\n 1: Soma \n 2: Subtração \n 3: Multiplicação \n 4: Divisão \n 0: sair")
    
    #bloco criado para testar se o usuário digita alguma coisa diferente de um número
    try:
        
        operacao = int(input()); #Recebe o número correspondete a operação

        # Se o número digitado correesponder a uma operação entra no if
        if((operacao >=1) and (operacao <=4)): 

            #recebe e converte os números que serão utilizados na operação desejada

            um = float(input("\nInforme o primeiro número para realizar a operação: "));

            dois = float(input("\nInforme o segundo número que será utilizado na operação: "));

            #Checa qual valor da operação, para imprimir o nome correto de cada uma delas no resultado
            match operacao:
                case 1:
                    print(f"\nO resultado da Soma dos números {um} e {dois} é: \n");
                case 2:
                    print(f"\nO resultado da Subtração dos números {um} e {dois} é: \n");
                case 3:
                    print(f"\nO resultado da Multiplicação dos números {um} e {dois} é: \n");
                case 4:
                    print(f"\nO resultado da Divisão dos números {um} e {dois} é: \n");

            #Chama a função e imprime o valor do resultado
            print(calculadora(um, dois, operacao));
            
            sleep(3) #pausa para que o resultado seja exibido na tela por 3 segundos

        elif(operacao == 0 ):
            break; #Se o usuário digitar "0", encerra o programa

        #Se for digitado um número diferente de 0, 1, 2, 3 e 4, exibe uma mensagem de alerta
        else: 

            print("\nNúmero inválido, por favor informar um número entre 0 e 4!!!")

            sleep(3) #pausa para que a mensagem seja exibida na tela por 3 segundos
            

        #Trantando o erro, se for digitado algo que não seja um número, exibe uma mensagem de alerta
    except:
            print("\nFavor digitar um NÚMERO válido, entre 0 e 4!!!")

            sleep(3) #pausa para que a mensagem seja exibida na tela por 3 segundos
