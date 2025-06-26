import random
import time
import os

print("+======================+")
print("| JOGO DO ALISTAMENTO  |")
print("+======================+")

print("Estamos em guerra, precisamos de soldados")
print("Você só pode alistar:")
print("- pessoas entre 18 e 40 anos;")
print("- indíviduos acima dos 50kg e menos de 100kg")
print("Há 10 voluntários, o exército conta com você")
print("Para cada acerto, você receberá uma comissão de R$10,00")
ok = input("Pressione qualquer tecla para continuar: ")

#dados no loop
contador = 1
permitidos = 0
recusados = 0
erros = 0
acertos = 0

while (contador<=10):
    os.system('clear')
    peso=random.randint(30,150)
    idade=random.randint(16,95)
    if(idade>50):
        idade=random.randint(16,70)
    if(peso>100):
        peso=random.randint(30,120)
    print("VOLUNTÁRIO N° %d" %contador)
    print("IDADE: %d anos" %idade)
    print("PESO: %d kg" %peso)
    print("+=========================+")
    print("|Permitir [1]   Recusar[2]|")
    print("+=========================+")
    print("Insira a opção:")
    opcao=int(input())
    if(opcao == 1):
       print("Você: Bem vindo ao exército!")
       permitidos+=1
       #análise de erro:
       if(idade>40 or idade<18):
           erros+=1
       elif(peso>100 or peso<50):
           erros+=1
       else:
           acertos+=1
           
    elif(opcao == 2):
        print("Você: Seu alistamento foi recusado")
        recusados+=1
        #análise de erro:
        if(idade>=18 and idade<=40 and peso>=50 and peso<=100):
            erros+=1
        else:
            acertos+=1
    else:
         print("ERRO NA TECLA, TENTE NOVAMENTE!")
         contador-=1
    time.sleep(2)
    contador+=1
   
grana=acertos*10             
print("+==========+")
print("|FIM DE JOGO|")
print("+==========+")
print("Permitidos: %d" %permitidos)
print("Recusados: %d" %recusados)
print("Deméritos: %d" %erros)
print("Comissão: R$%d" %grana)
