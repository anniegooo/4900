import pandas as pd
import math
import statistics

data=pd.read_csv('yg.csv')

date=data['Date']
n1=data['Open']
n2=data['High']
n3=data['Low']
n4=data['Close']
n5=data['Adj Close']
n6=data['Volume']

p=[]
for i in range(0,2939):
    p.append((1/4)*(2*n4[i]+n2[i]+n3[i]))

S50=[]
s50=[]
for i in range(2939,50,-1):
    for j in range(50,1,-1):
        s50.append(p[i-j])
    S50.append(min(s50))
    s50.clear()

S100=[]
s100=[]
for i in range(2939,100,-1):
    for j in range(100,1,-1):
        s100.append(p[i-j])
    S100.append(min(s100))
    s100.clear()

S200=[]
s200=[]
for i in range(2939,200,-1):
    for j in range(200,1,-1):
        s200.append(p[i-j])
    S200.append(min(s200))
    s200.clear()

R50=[]
r50=[]
for i in range(2939,50,-1):
    for j in range(50,1,-1):
        r50.append(p[i-j])
    R50.append(max(r50))
    r50.clear()

R100=[]
r100=[]
for i in range(2939,100,-1):
    for j in range(100,1,-1):
        r100.append(p[i-j])
    R100.append(max(r100))
    r100.clear()

R200=[]
r200=[]
for i in range(2939,200,-1):
    for j in range(200,1,-1):
        r200.append(p[i-j])
    R200.append(max(r200))
    r200.clear()


y50=[]
for t in range(50,2939):
    f=float(p[t])-float(R50[t-50])
    g=float(S50[t-50])-float(p[t])
    if f>0:
        y=1
    else:
        if g>0:
           y=-1
        else:
           y=0
    y50.append(y)

y100=[]
for t in range(100,2939):
    f=float(p[t])-float(R100[t-100])
    g=float(S100[t-100])-float(p[t])
    if f>0:
        x=1
    else:
        if g>0:
           x=-1
        else:
           x=0
    y100.append(x)

y200=[]
for t in range(200,2939):
    f=float(p[t])-float(R200[t-200])
    g=float(S200[t-200])-float(p[t])
    if f>0:
        z=1
    else:
        if g>0:
           z=-1
        else:
           z=0
    y200.append(z)
            
r50=[]
r=[]
for i in range(50,2889):
    if float(y50[i])!=0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r50.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()

r100=[]
r=[]
for i in range(50,2839):
    if float(y100[i])!=0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r100.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r200=[]
r=[]
for i in range(50,2739):
    if float(y200[i])!=0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r200.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r50b=[]
r=[]
for i in range(50,2889):
    if float(y50[i])>0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r50b.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r100b=[]
r=[]
for i in range(100,2839):
    if float(y100[i])>0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r100b.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r200b=[]
r=[]
for i in range(200,2739):
    if float(y200[i])>0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r200b.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r50s=[]
r=[]
for i in range(50,2889):
    if float(y50[i])<0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r50s.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r100s=[]
r=[]
for i in range(100,2839):
    if float(y100[i])<0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r100s.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r200s=[]
r=[]
for i in range(200,2739):
    if float(y200[i])<0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r200s.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


mr50s=statistics.mean(r50s)

mr100s=statistics.mean(r100s)

mr200s=statistics.mean(r200s)

mr50b=statistics.mean(r50b)

mr100b=statistics.mean(r100b)

mr200b=statistics.mean(r200b)

mr50=statistics.mean(r50)
mr100=statistics.mean(r100)
mr200=statistics.mean(r200)

v50=statistics.variance(r50)
v100=statistics.variance(r100)
v200=statistics.variance(r200)

t50s=(mr50s-mr200)/math.sqrt(((v50/len(y50))+(v50/(y50.count(-1)))))
t100s=(mr100s-mr200)/math.sqrt(((v100/len(y100))+(v100/(y100.count(-1)))))
t200s=(mr200s-mr200)/math.sqrt(((v200/len(y200))+(v200/(y200.count(-1)))))
t50b=(mr50b-mr50)/math.sqrt(((v50/len(y50))+(v50/(y50.count(1)))))
t100b=(mr100b-mr100)/math.sqrt(((v100/len(y100))+(v100/(y100.count(1)))))
t200b=(mr200b-mr200)/math.sqrt(((v200/len(y200))+(v200/(y200.count(1)))))

t50=(mr50b-mr50s)/math.sqrt((v50/(y50.count(1)))+(v50/(y50.count(-1))))
t100=(mr100b-mr100s)/math.sqrt((v100/(y100.count(1)))+(v100/(y100.count(-1))))
t200=(mr200b-mr200s)/math.sqrt((v200/(y200.count(1)))+(v200/(y200.count(-1))))


S50band=[]
s50band=[]
for i in range(2939,50,-1):
    for j in range(50,1,-1):
        s50band.append(p[i-j])
    S50band.append(0.99*min(s50band))
    s50band.clear()


S100band=[]
s100band=[]
for i in range(2939,100,-1):
    for j in range(100,1,-1):
        s100band.append(p[i-j])
    S100band.append(0.99*min(s100band))
    s100band.clear()


S200band=[]
s200band=[]
for i in range(2939,200,-1):
    for j in range(200,1,-1):
        s200band.append(p[i-j])
    S200band.append(0.99*min(s200band))
    s200band.clear()


R50band=[]
r50band=[]
for i in range(2939,50,-1):
    for j in range(50,1,-1):
        r50band.append(p[i-j])
    R50band.append(1.01*max(r50band))
    r50band.clear()


R100band=[]
r100band=[]
for i in range(2939,100,-1):
    for j in range(100,1,-1):
        r100band.append(p[i-j])
    R100band.append(1.01*max(r100band))
    r100band.clear()


R200band=[]
r200band=[]
for i in range(2939,200,-1):
    for j in range(200,1,-1):
        r200band.append(p[i-j])
    R200band.append(1.01*max(r200band))
    r200band.clear()


y=[]
y50band=[]
for t in range(50,2939):
    f=float(p[t])-float(R50band[t-50])
    g=float(S50band[t-50])-float(p[t])
    if f>0:
        y=1
    else:
        if g>0:
           y=-1
        else:
           y=0
    y50band.append(y)

x=[]
y100band=[]
for t in range(100,2939):
    f=float(p[t])-float(R100band[t-100])
    g=float(S100band[t-100])-float(p[t])
    if f>0:
        x=1
    else:
        if g>0:
           x=-1
        else:
           x=0
    y100band.append(x)

z=[]
y200band=[]
for t in range(200,2939):
    f=float(p[t])-float(R200band[t-200])
    g=float(S200band[t-200])-float(p[t])
    if f>0:
        z=1
    else:
        if g>0:
           z=-1
        else:
           z=0
    y200band.append(z)

  
r50band=[]
r=[]
for i in range(50,2889):
    if float(y50band[i])!=0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r50band.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r100band=[]
r=[]
for i in range(100,2839):
    if float(y100band[i])!=0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r100band.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r200band=[]
r=[]
for i in range(200,2739):
    if float(y200band[i])!=0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r200band.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r50bband=[]
r=[]
for i in range(50,2889):
    if float(y50band[i])>0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r50bband.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r100bband=[]
r=[]
for i in range(100,2839):
    if float(y100band[i])>0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r100bband.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r200bband=[]
r=[]
for i in range(200,2739):
    if float(y200band[i])>0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r200bband.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r50sband=[]
r=[]
for i in range(50,2889):
    if float(y50band[i])<0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r50sband.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r100sband=[]
r=[]
for i in range(100,2839):
    if float(y100band[i])<0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r100sband.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


r200sband=[]
r=[]
for i in range(200,2739):
    if float(y200band[i])<0:
        for j in range(0,10):
           mp=float(p[i+j])/float(p[i-1+j])
           if mp>0:
              r.append(math.log(mp))
           else:
              r.append(0)
        r200sband.append(float(r[0])+float(r[1])+float(r[2])+float(r[3])+float(r[4])+float(r[5])+float(r[6])+float(r[7])+float(r[8])+float(r[9]))   
        r.clear()


mr50sband=statistics.mean(r50sband)

mr100sband=statistics.mean(r100sband)

mr200sband=statistics.mean(r200sband)

mr50bband=statistics.mean(r50bband)

mr100bband=statistics.mean(r100bband)

mr200bband=statistics.mean(r200bband)

mr50band=statistics.mean(r50band)
mr100band=statistics.mean(r100band)
mr200band=statistics.mean(r200band)


v50band=statistics.variance(r50band)
v100band=statistics.variance(r100band)
v200band=statistics.variance(r200band)


t50sband=(mr50sband-mr200band)/math.sqrt(((v50band/len(y50band))+(v50band/(y50band.count(-1)))))
t100sband=(mr100sband-mr200band)/math.sqrt(((v100band/len(y100band))+(v100band/(y100band.count(-1)))))
t200sband=(mr200sband-mr200band)/math.sqrt(((v200band/len(y200band))+(v200band/(y200band.count(-1)))))
t50bband=(mr50bband-mr50band)/math.sqrt(((v50band/len(y50band))+(v50band/(y50band.count(1)))))
t100bband=(mr100bband-mr100band)/math.sqrt(((v100band/len(y100band))+(v100band/(y100band.count(1)))))
t200bband=(mr200bband-mr200band)/math.sqrt(((v200band/len(y200band))+(v200band/(y200band.count(1)))))

t50band=(mr50bband-mr50sband)/math.sqrt((v50band/(y50band.count(1)))+(v50band/(y50band.count(-1))))
t100band=(mr100bband-mr100sband)/math.sqrt((v100band/(y100band.count(1)))+(v100band/(y100band.count(-1))))
t200band=(mr200bband-mr200sband)/math.sqrt((v200band/(y200band.count(1)))+(v200band/(y200band.count(-1))))



a=[]
for i in range(0,969):
    if float(r50b[i])>0:
        a.append(r50b[i])
b50=len(a)/len(r50b)
a.clear()

a=[]
for i in range(0,len(r100b)):
    if float(r100b[i])>0:
        a.append(r100b[i])
b100=len(a)/len(r100b)
a.clear()

a=[]
for i in range(0,len(r200b)):
    if float(r200b[i])>0:
        a.append(r200b[i])
b200=len(a)/len(r200b)
a.clear()

a=[]
for i in range(0,len(r50s)):
    if float(r50s[i])>0:
        a.append(r50s[i])
s50=len(a)/len(r50s)
a.clear()

a=[]
for i in range(0,len(r100s)):
    if float(r100s[i])>0:
        a.append(r100s[i])
s100=len(a)/len(r100s)
a.clear()

a=[]
for i in range(0,len(r200s)):
    if float(r200s[i])>0:
        a.append(r200s[i])
s200=len(a)/len(r200s)
a.clear()

a=[]
for i in range(0,len(r50bband)):
    if float(r50bband[i])>0:
        a.append(r50bband[i])
b50band=len(a)/len(r50bband)
a.clear()

a=[]
for i in range(0,len(r100bband)):
    if float(r100bband[i])>0:
        a.append(r100bband[i])
b100band=len(a)/len(r100bband)
a.clear()

a=[]
for i in range(0,len(r200bband)):
    if float(r200bband[i])>0:
        a.append(r200bband[i])
b200bnad=len(a)/len(r200bband)
a.clear()

a=[]
for i in range(0,len(r50sband)):
    if float(r50sband[i])>0:
        a.append(r50sband[i])
s50band=len(a)/len(r50sband)
a.clear()

a=[]
for i in range(0,len(r100sband)):
    if float(r100sband[i])>0:
        a.append(r100sband[i])
s100band=len(a)/len(r100sband)
a.clear()

a=[]
for i in range(0,len(r200sband)):
    if float(r200sband[i])>0:
        a.append(r200sband[i])
s200band=len(a)/len(r200sband)
a.clear()

avb=(mr50b+mr100b+mr200b+mr50bband+mr100bband+mr200bband)/6
avs=(mr50s+mr100s+mr200s+mr50sband+mr100sband+mr200sband)/6
avbs=(mr50+mr100+mr200+mr50band+mr100band+mr200band)/6



print('buy signal of 50days',y50.count(1))
print('buy signal of 100days',y100.count(1))
print('buy signal of 200days',y200.count(1))
print('sell signal of 50days',y50.count(-1))
print('sell signal of 100days',y100.count(-1))
print('sell signal of 200days',y200.count(-1))

print('buy signal of 50days',y50band.count(1))
print('buy signal of 100days',y100band.count(1))
print('buy signal of 200days',y200band.count(1))
print('sell signal of 50days',y50band.count(-1))
print('sell signal of 100days',y100band.count(-1))
print('sell signal of 200days',y200band.count(-1))

print('b50',mr50b,'b100',mr100b,'b200',mr200b,'b.50',mr50bband,'b.100',mr100bband,'b.200',mr200bband,'s50',mr50s,'s100',mr100s,'s200',mr200s,'s.50',mr50sband,'s.100',mr100sband,'s.200',mr200sband)
print('                 ')
print('50>0',b50,s50,'50.>0',b50band,s50band,'100',b100,s100,'100.',b100band,s100band,'200',b200,s200,'200.',b200bnad,s200band)
print('                  ')
print('50',mr50,'100',mr100,'200',mr200,'50.',mr50band,'100.',mr100band,'200.',mr200band)
print('                ')
print(t50sband,t100sband,t200sband,t50bband,t100bband,t200bband,t50band,t100band,t200band)
print('                 ')
print(t50s,t100s,t200s,t50b,t100b,t200b,t50,t100,t200)
print(avb,avs,avbs)