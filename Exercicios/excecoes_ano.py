# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, 
#ou completará, no ano atual (2022).
# Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
#o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


from time import sleep;

nome = input("\nInforme seu nome completo: ");
while True:
    try:
        ano = int(input("\nInforme o ano do seu nascimento: \n\nOBS: O ano precisar estar entre 1922 e 2021! "));
        if((ano >= 1922) and (ano <= 2021)):
            idade = 2022 - ano;
            print(f"\n{nome} este ano você completa ou completou {idade} anos\n");
            sleep(2);
            break;
        else:
            print("\nANO INVÁLIDO!!!, informe um ano entre 1922 e 2021\n")
            sleep(2);
            continue;
    except:
            print("\nANO INVÁLIDO!!!, informe um ano entre 1922 e 2021\n")
            sleep(2);