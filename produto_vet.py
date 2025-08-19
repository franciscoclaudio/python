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
    
vetor1=list(range(3))
vetor2=list(range(3)) 
vetor1=[1,1,1]
vetor2=[1,1,-1]

print("\no produto escalar é",prod_esc(vetor1,vetor2))
print("\no produto vetorial é",prod_vet(vetor1,vetor2))
print("\na projeção de",vetor1, "na direção de ",vetor2, " é:\n",proj(vetor1,vetor2))
print("\na altura do paralelogramo formado por ",vetor1, " e ", vetor2, " é:\n",alt(vetor1,vetor2), " com módulo: ",mod(alt(vetor1,vetor2)))
print("\nFim do código.\n")

