import math

def escolhe(n, k):
  return math.comb(n, k)

def calc(p,a,s,n):
    soma=0
    soma1=0
    Probabilidade_exata=list(range(s+1))
    Probabilidade_pelo_menos=list(range(s+1))
    for i in range (int(s+1)):
        print(p-s,a-i)
        teste=escolhe((p-s),(a-i))/escolhe(p,s)
        teste=teste*(escolhe(s,i))
        soma=soma+teste
        Probabilidade_exata[i] = teste
        Probabilidade_pelo_menos[i] = soma
        #print(soma)
    
    for j in range (len(Probabilidade_exata)):
        if j==n:
            print("CHANCE DE EXATAMENTE", j, "SUCESSOS:", Probabilidade_exata[j], "\tCHANCE DE PELO MENOS", j, "SUCESSOS:", 1-soma1)
        soma1+=Probabilidade_exata[j]
    """
    teste=(escolhe(s,n)*escolhe((p-s),(a-n)))/escolhe(p,s)
    soma=soma+teste
    """
    return [Probabilidade_exata[n],Probabilidade_pelo_menos[n]] 

"""
P=int(input('tamanho da população:\n'))
A=int(input('\ntamanho da amostra:\n'))
S=int(input('\nsucessos na população:\n'))
N=int(input('\nsucessos necessários:\n'))
"""
P=50    
A=10    
S=5
N=4
vetor=calc(P,A,S,N)
