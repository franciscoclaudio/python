D=int(1)
M=int(1)
Y=int(2016)

DATA=[D,M,Y]

D1=int(31)
M1=int(12)
Y1=int(2016)

DATA1=[D1,M1,Y1]


def checa_bissesto(date):
    teste=date[2]
    if teste % 4 == 0:
        if teste % 100 == 0:
            if teste % 400 == 0:
                return 1
            else: return 0
        else:
            return 1
    else: return 0            

def dda(date):
    d1,m1=date[0],0
    if date[1]==1:
        m1=0
    if date[1]==2:
        m1=31
    if date[1]==3:
        m1=31+checa_bissesto(date)+28
    if date[1]==4:
        m1=59+checa_bissesto(date)+31
    if date[1]==5:
        m1=90+checa_bissesto(date)+30
    if date[1]==6:
        m1=120+checa_bissesto(date)+31
    if date[1]==7:
        m1=151+checa_bissesto(date)+30
    if date[1]==8:
        m1=181+checa_bissesto(date)+31
    if date[1]==9:
        m1=212+checa_bissesto(date)+31
    if date[1]==10:
        m1=243+checa_bissesto(date)+30
    if date[1]==11:
        m1=273+checa_bissesto(date)+31
    if date[1]==12:
        m1=304+checa_bissesto(date)+30
    return (d1+m1)


def dda2date(x,year):
    date = [0,0,year]
    b=checa_bissesto([1,1,year])
    if x<=31:
        date[0]=x
        date[1]=1
    if x>31 and x<=59+b:
        date[0]=x-31
        date[1]=2
    if x>59+b and x<=90+b:
        date[0]=x-59- b
        date[1]=3
    if x>90+b and x<=120+b:
        date[0]=x-90- b
        date[1]=4
    if x>120+b and x<=151+b:
        date[0]=x-120- b
        date[1]=5
    if x>151+b and x<=181+b:
        date[0]=x-151- b
        date[1]=6
    if x>181+b and x<=212+b:
        date[0]=x-181- b
        date[1]=7  
    if x>212+b and x<=243+b:
        date[0]=x-212- b
        date[1]=8      
    if x>243+b and x<=273+b:
        date[0]=x-243- b
        date[1]=9
    if x>273+b and x<=304+b:
        date[0]=x-273- b
        date[1]=10
    if x>304+b and x<=334+b:
        date[0]=x-304- b
        date[1]=11
    if x>334+b and x<=365+b:
        date[0]=x-334- b
        date[1]=12
    return date
            
def dif_semana(date,semana_atual,semana_escolhida):
    d1=date
    sa=semana_atual
    se=semana_escolhida
    x=dda(d1)+7*(se-sa)
    return dda2date(x,date[2])
    
def dc(date):
    x=dda(date)
    y=date[2]
    s=0
    c=0
    for i in range (0,(y-1)):
        c=c+1
        s=s+365+checa_bissesto([1,1,i])
    dia_corrido=s+x
    if date[1]==2:
        if date[0]>=28:
            dia_corrido=dia_corrido + checa_bissesto(date)
    if date[1]>2:
        dia_corrido=dia_corrido + checa_bissesto(date)
    return dia_corrido

def dif_dias(date0,date1):
    x=dc(date0)
    print(x)
    y=dc(date1)
    print(y)
    print(x-y)
    print(y-x)
    if x>y:
        return (x-y)
    else:
        return (y-x)
#print (dif_semana([8,1,2025],14,37))

print(dif_dias(DATA,DATA1))
