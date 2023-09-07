# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

# Escreva um código que imprima todos os números exceto o número 13.
# Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

#Crescente usando o for
print("\nCrescente utilizando o for!!\n")
for i in range(20):
	if(i==12):
		continue;
	print(f"{i+1} andar");


print("\n########################\n")

######################################
#Crescente usando o while	
print("\nCrescente utilizando o while!!\n")
i=1;
while(i <= 21):
  if(i==13):
    pass;
  else:
	  print(f"{i} andar");
  i = i + 1;
  

print("\n########################\n")

######################################
#Decrescente usando o for
print("\Decrescente utilizando o for!!\n")
for i in range(21, 1, -1):
	if(i==14):
		continue;
	print(f"{i-1} andar");


print("\n########################\n")

######################################
#Decrescente usando o while	
print("\Decrescente utilizando o while!!\n")
i=20;
while(i >= 1):
  if(i==13):
    pass;
  else:
	  print(f"{i} andar");
  i = i - 1;