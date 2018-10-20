# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:44:08 2015

@author: victor
"""

#module de fonctions concercenants l'utilisation de droites et des coordonées cartésiennes

import matplotlib.pyplot as plt
import numpy as np
from global_variables import rp

def traceDroite(p1,p2,couleur="noir"):
    x1,x2,y1,y2=p1[0],p2[0],p1[1],p2[1]
    if couleur=="noir":
        plt.plot([x1,x2],[y1,y2],color="black")
    if couleur=="rouge":
        plt.plot([x1,x2],[y1,y2],color="red")
    if couleur=="vert":
        plt.plot([x1,x2],[y1,y2],color="green")
    if couleur=="bleu":
        plt.plot([x1,x2],[y1,y2],color="blue")
    
def intersectionDroites(p1,p2,i=0):
    if i==0:
        a1,b1=creaDroite(p1)
        a2,b2=creaDroite(p2)
        if a1!=a2 :
            x=(b2-b1)/(a1-a2)
            y=a1*x+b1
            return([x,y,1])
        else:
            return([0,0,0])
    else:
        a1,b1=creaDroite(p1)
        a2,b2=creaDroite(p2,i=1)
        if a1!=a2 :
            x=(b2-b1)/(a1-a2)
            y=a1*x+b1
            return([x,y,1])
        else:
            return([0,0,0])
            
def creaDroite(p,i=0):
    if i==0:
        a=(p.dy()/p.dx() if p.dx()!=0 else 10**5)
        b=p.y()-a*p.x()
        return([a,b])
    else:
        a=(p[3]/p[2] if p[2]!=0 else 10**5)
        b=p[1]-a*p[0]
        return([a,b])

def distancePoints(p1,p2):
    return(np.sqrt(np.square(p1[0]-p2[0])+np.square(p1[1]-p2[1])))

def distancePointsP(p1,p2):
    return(distancePoints([p1.x(),p1.y()],[p2.x(),p2.y()]))   

def intersectionCercle(p,i,obstacles):
    xc,yc=obstacles[i][0]
    r=obstacles[i][1]
    R=r+rp
    a,b=creaDroite(p)
    x,y=p.position()
    A=np.square(a)+1
    B=2*( a*(b-yc) - xc )
    C=np.square(b-yc)-np.square(R)+np.square(xc)
    delta = B**2-4*A*C
    solutions = ["n","n"]
    if delta>=0:
        x1,x2=(-B + np.sqrt(delta))/(2*A),(-B - np.sqrt(delta))/(2*A)
        solutions = [ [ x1 , a*x1+b ] , [ x2 , a*x2 + b ] ]
    return( (delta>=0 and x2+0.1<x)  , solutions )