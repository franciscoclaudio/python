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
    print("4. Altura do Parallelogramo")
    print("5. Equação do Plano")
    print("6. Módulo de Vetor")
    print("7. Soma de Vetores")
    print("8. Subtração de Vetores")
    print("9. Distância Ponto ao Plano")
    print("10. Distância Ponto à Reta")
    print("11. Sair do programa")

def opcao_1_acao():
    print("Você escolheu a opção: produto escalar\n")
    v1=ler_vet()
    v2=ler_vet()
    k=prod_esc(v1,v2)    
    print("\nO produto escalar é: ", k)
   
def opcao_2_acao():
    print("Você escolheu a opção: produto vetorial\n")
    v1=ler_vet()
    v2=ler_vet()
    k=prod_vet(v1,v2)    
    print("\nO produto vetorial é: ", k)

def opcao_3_acao():
    print("Você escolheu a opção: Projeção\n")
    v1=ler_vet()
    v2=ler_vet()
    k=proj(v1,v2)    
    print("\nA projeção de v1 na direção de v2 é: ", k)

def opcao_4_acao():
    print("Você escolheu a opção: Altura do Parallelogramo\n")
    v1=ler_vet()
    v2=ler_vet()
    altura=alt(v1,v2)
    print("\nA altura é: ", altura, "com módulo: ", mod(altura))

def opcao_5_acao():
    print("Você escolheu a opção: Equação do Plano\n")
    v1=ler_vet()
    v2=ler_vet()
    p=ler_vet()
    eq=equacao_plano(v1,v2,p)
    print("\nA equação do plano é: ", eq)

def opcao_6_acao():
    print("Você escolheu a opção: Módulo de Vetor\n")
    v1=ler_vet()
    print("\nO módulo do vetor é: ", mod(v1))

def opcao_7_acao():
    print("Você escolheu a opção: Soma de Vetores\n")
    v1=ler_vet()
    v2=ler_vet()
    print("\nA soma dos vetores é: ", soma_vet(v1,v2))

def opcao_8_acao():
    print("Você escolheu a opção: Subtração de Vetores\n")
    v1=ler_vet()
    v2=ler_vet()
    print("\nA subtração dos vetores é: ", sub_vet(v1,v2))

def opcao_9_acao():
    print("Você escolheu a opção: Distância Ponto ao Plano\n")
    p=ler_vet()
    n=ler_vet()
    d=float(input("Digite o parâmetro d do plano: "))
    print("\nA distância do ponto ao plano é: ", distancia_ponto_plano(p,n,d))

def opcao_10_acao():
    print("Você escolheu a opção: Distância Ponto à Reta\n")
    P=ler_vet()
    Po=ler_vet()
    V=ler_vet()
    resultado, dist = distancia_ponto_reta(P,Po,V)
    print("\nO vetor distância é: ", resultado)
    print("A distância é: ", dist)

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
        opcao_4_acao()
    elif choice == '5':
        opcao_5_acao()
    elif choice == '6':
        opcao_6_acao()
    elif choice == '7':
        opcao_7_acao()
    elif choice == '8':
        opcao_8_acao()
    elif choice == '9':
        opcao_9_acao()
    elif choice == '10':
        opcao_10_acao()
    elif choice == '11':
        print("Sair do Programa.")
        break
    else:
        print("Escolha errada. Por favor tente de novo.")
