def soma(n1, n2):
    print(n1 + n2)
def subtracao(n1, n2):
    print(n1 - n2)
    
 def divisao(n1, n2):
    print(n1 / n2) 

print("             calculadora")
print("selecione o numero da operação")

print("1 - soma")
print("2 - subtração")
print("3 - divisão")
print("4 - Multiplicação")
print("<<<<<<<< >>>>>>>>>")
opcao = input("escolha uma opção (1/2/3/4) : ")
n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo  numero: "))
 
if opcao == '1':
      soma(n1,n2)
        
elif opcao == '2':
     subtração(n1,n2)      
            
elif opcao == '3':
     divisao(n1,n2)
            
else:
     multplicacao(n1,n2)
                
             
              