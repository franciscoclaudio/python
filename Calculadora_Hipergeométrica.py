'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import math
from scipy.special import loggamma

def hypergeometric_log_prob(N, n, K, k):
    # log P(X=k) = log(C(K, k)) + log(C(N-K, n-k)) - log(C(N, n))
    # log C(n, k) = log(n!) - log(k!) - log((n-k)!)
    # Using loggamma(x+1) = log(x!)

    log_comb_K_k = loggamma(K + 1) - loggamma(k + 1) - loggamma(K - k + 1)
    log_comb_NK_nk = loggamma(N - K + 1) - loggamma(n - k + 1) - loggamma(N - K - (n - k) + 1)
    log_comb_N_n = loggamma(N + 1) - loggamma(n + 1) - loggamma(N - n + 1)

    return log_comb_K_k + log_comb_NK_nk - log_comb_N_n

def escolhe(x,y):
    log_comb_x_y = loggamma(x + 1) - loggamma(y + 1) - loggamma(x - y + 1)  
    return log_comb_x_y

    

def calc(p,a,s,n):
    Probabilidade_exata=list(range(s+1))
    Probabilidade_pelo_menos=list(range(s+1))
    soma=0
    for i in range (int(s+1)):
        teste=hypergeometric_log_prob(p, a, s, i)
        Probabilidade_exata[i] = teste
        #print(soma)
    
    for j in range (len(Probabilidade_exata)):
        soma=soma+math.exp(Probabilidade_exata[j])
        Probabilidade_pelo_menos[j] = soma
        if j==n:
            pe=math.exp(Probabilidade_exata[j])
            pp=(1-soma)
            print("CHANCE DE EXATAMENTE", j, f"SUCESSOS: {pe:.5f}")
            print("CHANCE DE PELO MENOS", j, f"SUCESSOS: {pp:.5f}")
    """
    teste=(escolhe(s,n)*escolhe((p-s),(a-n)))/escolhe(p,s)
    soma=soma+teste
    """
    return [math.exp(Probabilidade_exata[n]), Probabilidade_pelo_menos[n]] 

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
#prob = math.exp(hypergeometric_log_prob(P,A,S,N))
#print(prob)
vetor=calc(P,A,S,N)