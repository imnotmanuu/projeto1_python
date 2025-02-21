print("********************************")
print ("bem vindo ao jogo da advinhação")
print("********************************") 
 
chute = int(input("digite o seu número: ")) 

numero_secreto = 27 
acertou = numero_secreto == chute 
chute_maior  = chute > numero_secreto
chute_menor = chute < numero_secreto


print(f"Você digitou {chute}")

if(numero_secreto == chute):
  print("você acertou!")
else:
    if(chute > numero_secreto):
     print("Você errou! Seu número foi maior do que o número secreto ") 


print("@@@@@@@@@@@")
print("fim de jogo")
print("@@@@@@@@@@@")
   
   