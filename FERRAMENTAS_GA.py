import math

def prod_esc(v1,v2):
    esc=0
    for i in range(len(v1)):
    	x=float(v1[i])
    	y=float(v2[i])
    	esc=esc + x*y
    return esc

def prod_vet(v1,v2):
    vet=list(range(len(v1)))
    vet[0]=v1[1]*v2[2]-v1[2]*v2[1]
    vet[1]=-((v1[0]*v2[2])-(v1[2]*v2[0]))
    vet[2]=v1[0]*v2[1]-v1[1]*v2[0]
    return vet

def mod(v1):
    modulo=0
    for i in range(len(v1)):
    	modulo=modulo+(v1[i]*v1[i])
    return math.pow(modulo,0.5)

def proj(v1,v2):
    projecao=list(range(len(v1)))
    alpha=prod_esc(v1,v2)/(mod(v2)*mod(v2))
    for i in range(len(v1)):
    	projecao[i]=alpha*v2[i]
    return projecao

def alt(v1,v2):
    alt=list(range(len(v1)))
    projecao=proj(v1,v2)
    for i in range(len(v1)):
    	alt[i]=v1[i]-projecao[i]
    return alt
    
def equacao_plano(v1,v2,p):
    diretor=prod_vet(v1,v2)
    d=-(diretor[0]*p[0]+diretor[1]*p[1]+diretor[2]*p[2])
    v=[diretor[0],diretor[1],diretor[2],d]
    return v
def print_vet(v):
    texto=""
    texto=texto+ str(f"[{v[0]:.5f}, ")+ str(f"{v[1]:.5f}, ")+ str(f"{v[2]:.5f}]")
    return texto
def distancia_ponto_plano(p,n,d):
    mod=0
    n1=0
    for i in range (len(p)):
    	mod=mod+(n[i]*p[i])
    	n1=n1+(n[i]*n[i])
    mod=mod+d
    mod=abs(mod)/math.pow(n1,0.5)
    return mod
def soma_vet(v1,v2):
    v=[0,0,0]
    for i in range(len(v1)):
    	v[i]=v1[i]+v2[i]
    return v

def ler_vet():
    v=[0,0,0]
    v2=['i','j','k']
    for i in range(3):
    	v[i]=float(input("insira a componente "+str(v2[i])+": \n"))
    return v
def sub_vet(v1,v2):
    v=[0,0,0]
    for i in range(len(v1)):
    	v[i]=v1[i]-v2[i]
    return v

def distancia_ponto_reta(P,Po,V):
    v1=[0,0,0]
    vetor=sub_vet(P,Po)
    v1=alt(vetor,V)
    return v1,mod(v1)
    
def exibir_menu():
    print("\n--- menu principal ---")
    print("1. Produto Escalar")
    print("2. Produto Vetorial")
    print("3. Projeção")
    print("4. Sair do programa")

def opcao_1_acao():
    print("Você escolheu a opção: produto escalar\n")
    print("\nInsira o primeiro vetor:\n")
    v1=ler_vet()
    print("\nInsira o segundo vetor:\n")
    v2=ler_vet()
    k=prod_esc(v1,v2)    
    print("\nO produto escalar é: ", k)
   
def opcao_2_acao():
    print("Você escolheu a opção: produto vetorial\n")
    print("\nInsira o primeiro vetor:\n")
    v1=ler_vet()
    print("\nInsira o segundo vetor:\n")
    v2=ler_vet()
    k=prod_vet(v1,v2)    
    print("\nO produto vetorial é: ", k)

    
def opcao_3_acao():
    print("Você escolheu a opção: Projeção\n")
    print("\nInsira o primeiro vetor:\n")
    v1=ler_vet()
    print("\nInsira o segundo vetor:\n")
    v2=ler_vet()
    k=proj(v1,v2)    
    print("\nA projeção de v1 na direção de v2 é: ", k)


while True:
    exibir_menu()
    choice = input("Qual a sua escolha \n")

    if choice == '1':
        opcao_1_acao()
    elif choice == '2':
        opcao_2_acao()
    elif choice == '3':
    	opcao_3_acao()
    elif choice == '4':
        print("Sair do Programa.")
        break
    else:
        print("Escolha errada. Por favor tente de novo.")
 
    
"""
vetor1=list(range(3))
vetor2=list(range(3)) 
vetor1=[1,2,3]
vetor2=[1,1,0]
p1=[0,0,0]
print("\nos vetores a ser estudados são:\n\n",print_vet(vetor1),'e',print_vet(vetor2),'\n')
print("o ponto do plano é: ",p1)

print("\no produto escalar é",prod_esc(vetor1,vetor2))
print("\no produto vetorial é",prod_vet(vetor1,vetor2))
proje=proj(vetor1,vetor2)
print(f"\na projeção de v1, na direção de v2 é:\n\n", print_vet(proje))
altura=alt(vetor1,vetor2)

print("\na altura do paralelogramo formado por v1  e v2 é:\n\n",print_vet(altura), " com módulo: ", mod(alt(vetor1,vetor2)))
eq=equacao_plano(vetor1,vetor2,p1)
print("\nO vetor normal é: ", print_vet(prod_vet(vetor1,vetor2)))
print("\n"f"a equação do plano é: {eq[0]:.5f}*X + ",f"{eq[1]:.5f}*Y + ",f"{eq[2]:.5f}*Z + ", f"{eq[3]:.5f} = 0\n")
print("\nFim do código.\n")
"""
"""
P= [1,1,-1]
N= [2,1,-1]
d=-16
"""
"""
A=[2,1,0]
B=[1,0,2]
V = sub_vet(B,A)
C = [0,-1,-1]
"""

"""
print(distancia_ponto_plano(P,N,d))
print(2*math.pow(6,0.5))
"""
