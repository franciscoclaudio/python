import math
import webbrowser

def hypergeometric_log_prob(N, n, K, k):
    log_comb_K_k = escolhe(K,k)
    log_comb_NK_nk = escolhe (N-K,n-k)
    log_comb_N_n = escolhe(N,n)

    return log_comb_K_k + log_comb_NK_nk - log_comb_N_n

def escolhe(x,y):
    log_comb_x_y = fat(x) - fat(y) - fat(x - y)  
    return log_comb_x_y

def fat(x):
    i=0
    soma=0
    while i<x:
        soma=soma+math.log(x-i)
        i=i+1
    return soma
    

def calc(p,a,s,n,file1):
    html_temp="""<html>
    <head>
    <title>Calculadora Hipergeometrica</title>
    </head>
    <body>
    <h2>Bem vindo a minha Calculadora Hipergeometrica!</h2>
    """
    Probabilidade_exata=list(range(s+1))
    Probabilidade_pelo_menos=list(range(s+1))
    soma=0
    for i in range (int(s+1)):
        teste=hypergeometric_log_prob(p, a, s, i)
        Probabilidade_exata[i] = teste
        #print(soma)
    
    for j in range (len(Probabilidade_exata)):
        soma=soma+math.exp(Probabilidade_exata[j])
        pp=(1-soma)
        if j==n:
            pe=math.exp(Probabilidade_exata[j])
            html_temp=html_temp+"<p>CHANCE DE EXATAMENTE "+ str(j)+ str(f" SUCESSOS: {100*pe:.5f}%</p>")
            html_temp=html_temp+"<p>CHANCE DE PELO MENOS " + str(j) + str(f" SUCESSOS: {100*(pp+pe):.5f}%</p>")
        Probabilidade_pelo_menos[j] = soma
    html_temp=html_temp+("</body> </html>")
    file1.write(html_temp)

    return [math.exp(Probabilidade_exata[n]), Probabilidade_pelo_menos[n]] 

P=int(input('\ntamanho da população:\n'))
A=int(input('\ntamanho da amostra:\n'))
S=int(input('\nsucessos na população:\n'))
N=int(input('\nsucessos necessários:\n'))

html_file_path='/home/tenfranciscoclaudio/Downloads/Calculadora.html'

f = open(html_file_path, 'w')

"""
P=60
A=7
S=32
N=4
"""
vetor=calc(P,A,S,N,f)

f.close()

url = f"file://{html_file_path}"
webbrowser.open_new_tab(url)

print("\nfim do código.\n")


