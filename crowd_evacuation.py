# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:42:23 2016

@author: victor ruelle
"""


import matplotlib.pyplot as plt
import numpy as np
import os
from person import Person,calcAngle,invalid_movement,init,compression
from global_variables import step,walls
from gen_functions import getTime
from solving_blockings import unblock
from save_data import updateInfo

def one_time_step(X,Y,obstacles,count=0):
    # every person takes a single step
    Y.sort()
    Y.reverse()
    mvt=0
    for i in range(len(X)):
        k = Y[i][1]
        P = X[k]
        p, fini = P
        if not(fini):
#            calcAngle(p)
            mvt=single_step(X,k,obstacles)
            finished = p.x()<=0
            if finished:
                X[k][1] = True
                X[k][0].blocked = False
            else:
                #X[k][1] = False # should always be true
                Y[i][0]=p.distance_to_exit()
                calcAngle(p,obstacles)
    count=count_blocked_occurences(X)
    return mvt,count
    
def single_step(X,k,obstacles):
    p=X[k][0]
    for i in range(1,4):       
        p.avancer(step/i)
        if not(invalid_movement(X,k,obstacles)):
            p.blocked=False
            return(step/i)
        p.avancer(-step/i)
        p.shift(step/i,30)
        if not(invalid_movement(X,k,obstacles)):
            p.blocked=False
            return(step/i)
        p.shift(-step/i,30)
        p.shift(step/i,-30)
        if not(invalid_movement(X,k,obstacles)):
            p.blocked=False
            return(step/i)
        p.shift(-step/i,-30)
        p.shift(step/i,60)
        if not(invalid_movement(X,k,obstacles)):
            p.blocked=False
            return(step/i)
        p.shift(-step/i,60)
        p.shift(step/i,-60)
        if not(invalid_movement(X,k,obstacles)):
            p.blocked=False
            return(step/i)
        p.shift(-step/i,-60)
        p.blocked=True
        return(0)
    
def count_blocked_occurences(X):
    count = 0
    for i in range(len(X)):
        p=X[i][0]
        if p.blocked:
            count+=1
    return count

def checkRun(X):
    for i in range(len(X)):
        if not(X[i][1]):
            return True
    return False

def simulation(N,obstacles,save=False):
    # runs until everyone has evacuated or cannot move 
    if save:
        exp_no=getTime()
        print("images will be saved to output/"+str(exp_no))
        if not os.path.exists("output/"+str(exp_no)):
            os.makedirs("output/"+str(exp_no))
    X, Y = init(N,obstacles)
    s=0
    count = 0
    no_blocked = 0
    run = True
    while run == True :
        count+=1
        mvt,no_blocked = one_time_step(X,Y,obstacles,no_blocked)
        run = checkRun(X)
        unblock(X,obstacles)
        if save:
            save_image(X,count,obstacles,exp_no)
        if mvt==0:
            s+=1
            if s==2:
                return(0,no_blocked)
    return count,no_blocked
    
#save_image
    
def save_image(X,i,obstacles,exp_no):
    plt.close( )
    fig, ax = plt.subplots()
    for k in range(len(X)):
        P = X[k]
        p=P[0]
        comp = compression(X,k)
        if not(P[1]):
            p.disp(ax,compression=comp)
    for e in range( len(walls) ):
        xi,xs,yi,ys= walls[e][0][0], walls[e][1][0] , walls[e][0][1] , walls[e][1][1]
        plt.plot([xi,xs],[yi,ys],color='black')
    for o in obstacles:
        xc,yc=o[0]
        r=o[1]
        p=Person(xc,yc,rayonPropre=r)
        p.disp(ax,'k')        
    plt.title(str(i))
    plt.xlim(-1,10)
    plt.ylim(-2,9) 
    plt.axis('off')  
    plt.savefig('output/'+str(exp_no)+'/'+str(i))

#EXPERIMENTS

def experience(nombreAttendu,ecartAttendu,configuration,essais,path):
    N=[nombreAttendu-ecartAttendu]
    for i in range( N[0]+1 , nombreAttendu+ecartAttendu + 1 ):
        N.append(i)
    for n in N:
        Temps,Blocs,No,W=[],[],[],[]
        No.append(n)
        sumt=0
        sumb=0
        for k in range(essais):
            A=simulation(n,configuration)
            sumt+=(A[0] if A[0]!=0 else 0)
            sumb+=(A[1] if A[0]!=0 else 0) 
        Temps.append(sumt/essais)
        Blocs.append(sumb/essais)
        W.append(essais)
        updateInfo(No,Temps,Blocs,W,path)