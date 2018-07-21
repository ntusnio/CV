z=-1*3

t=[]
file=open("AC20-Institute-Var-2.obj", "r")
f=file.readlines()
file.close()
k=0
for line in f:
    if line[:6]=="usemtl":
        k+=1
        print(line+"("+str(k)+")")
    if line[:2]=="v ":
        l=line.split()
        if float(l[-1])==z:
            t.append([float(l[1]),float(l[2]),k])

import turtle

def prostokat(x1,x2,y1,y2):
    x1*=10
    x1-=200
    x2*=10
    x2-=200
    y1*=10
    y2*=10
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y1)
    turtle.goto(x2,y2)
    turtle.goto(x1,y2)
    turtle.goto(x1,y1)
    return

for i in range(k):
    x=[]
    y=[]
    for j in t:
        if j[2]==i:
            x.append(j[0])
            y.append(j[1])
    if len(x)>0:
        xx=max(x)-min(x)
        yy=max(y)-min(y)
        print(round(xx,2),"x",round(yy,2))
        if xx>yy:
            x=sorted(set(x))
            print(x,min(y),max(y))
            if yy<1 and yy>0.1 and xx>1.5:
                for n in range(1,len(x)):
                    if abs(x[n]-x[n-1]-1)>0.1: # drzwi poziome
                        prostokat(x[n-1],x[n],min(y),max(y))
        if yy>xx:
            y=sorted(set(y))
            print(min(x),max(x),y)
            if xx<1 and xx>0.1 and yy>1.5:
                for n in range(1,len(y)):
                    if abs(y[n]-y[n-1]-1.8)>0.1: # drzwi pionowe
                        prostokat(min(x),max(x),y[n-1],y[n])

import time
time.sleep(10)
