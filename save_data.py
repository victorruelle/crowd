import csv
import numpy as np
import matplotlib.pyplot as plt
from gen_functions import getTime

def saveInf(N,Tours,Blocs,Weight,info,path):
    w=open(str(path)+str(info)+".csv","w")
    w.write("N ; Tours ; Blocs ; Weight \n")
    for i in range(len(Tours)):
        w.write(str(N[i])+";"+str(Tours[i])+";"+str(Blocs[i])+";"+str(Weight[i])+"\n")
    w.close()

def recoverInfo(path):
    fichier=open(path+".csv",'r')
    content=fichier.readlines()
    lignes=[]
    for l in content:
        l=l.rstrip().split(";")
        lignes.append(l)
    no=np.linspace(1,150,150)
    for i in range(150):
        no[i]=int(no[i])
    no=list(no)
    t,b,w=list(np.zeros(150)),list(np.zeros(150)),list(np.zeros(150))
    lignes[1:].sort()
    for i in range(1,len(lignes)):
        n=int(float(lignes[i][0]))
        j=no.index(n)
        t[j]=float(lignes[i][1])
        b[j]=float(lignes[i][2])
        w[j]=float(lignes[i][3])
    return no,t,b,w

def updateInfo(N,T,B,W,path):
    no,t,b,w=recoverInfo(str(path)+"/simulations")
#    saveInf(no,t,b,w,time,path+"/recup")
    for n in N:
        j=N.index(n)
        i=no.index(n)
        t[i]=(W[j]*T[j]+w[i]*t[i])/(W[j]+w[i])
        b[i]=(W[j]*B[j]+w[i]*t[i])/(W[j]+w[i])
        w[i]+=W[j]
    fichier=open(str(path)+"/simulations",'w')
    fichier.flush()
    fichier.close()
    f=open(str(path)+"/simulations.csv","w")
    f.write("N ; Tours ; Blocs ; Weight \n")
    for i in range(len(t)):
        f.write(str(no[i])+";"+str(t[i])+";"+str(b[i])+";"+str(w[i])+"\n")
    f.close()   
    
def plotInfo(path):
    n,t,b,w=recoverInfo(str(path)+"/simulations")
    N,T,B=[],[],[]
    for i in range(len(n)):
        if n[i]!=0:
            N.append(n[i])
            T.append(t[i])
            B.append(b[i])
    plt.figure()
    L=path.split("/")
    config=L[len(L)-2]
    plt.title("évolution du temps d'évacuation en fonction du nombre de Persons pour la configuration "+str(config))
    plt.plot(N,T)
    plt.xlim(0,150)
    plt.figure()    
    plt.title("évolution du nombre de blocages en fonction du nombre de Persons pour la configuration "+str(config))
    plt.plot(N,B)