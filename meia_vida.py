m=float(input("\nDigite a nassa inicial em gramas:\n"))
n=m
cont=0
meia_vida=50

while n>0.5:
	cont+=1
	n=n/2
print("\nA massa inicial é: ",m)
print("\nA massa final é: ",n)

ts=meia_vida*cont
h=(int(ts/3600))
aux=(ts/3600)-h
min=int(60*aux)
seg=(60*aux)-min
seg=60*(seg)
print("\nO tempo passado foi: ", h," horas ", min, " minutos ", seg, " segundos ")
