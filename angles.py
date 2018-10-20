# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:46:17 2015

@author: victor
"""

import numpy as np
from gen_functions import signe


def getAngle(dx,dy):
    theta=((np.arctan(dy/(dx)) if dx>0 else np.arctan(dy/(dx))+signe(dy)*np.pi) if dx!=0 else signe(dy)*np.pi/2)
    return((theta if theta>=0 else 2*np.pi+theta)%(2*np.pi))
    
def distanceAngle(t1,t2):
    return(min(np.abs(t2-t1),2*np.pi-np.abs(t2-t1)))
      
def angleInBetween(a,al1,al2,para=0,strict='false'):
    #si para=0 alors a devra être entre al1 et al2 au sens court
    dl,d1,d2=distanceAngle(al2,al1),distanceAngle(a,al1),distanceAngle(a,al2)
    d1,d2=np.floor(d1*1000)/1000,np.floor(d2*1000)/1000
    if para==0:
        if strict=='false':
            if d1+d2<=dl:
                return(True)
            return(False)
        else:
            if d1+d2<=dl and a!=al1 and a!=al2:
                return(True)
            return(False)            
    else:
        if strict=='false':
            if d1+d2>dl:
                return(True)
            return(False)
        else:
            if d1+d2>=dl and a!=al1 and a!=al2:
                return(True)
            return(False)    
    
def angleInBetweenOld(a,al1,al2,para=0,strict='false'):
    #si para=0 alors a devra être entre al1 et al2 au sens court
    angle=distanceAngle(al1,al2)
    if para==0:
        if strict=='false':
            if distanceAngle(a,al1)+distanceAngle(a,al2)<=angle:
                return(True)
            return(False)
        else:
            if distanceAngle(a,al1)+distanceAngle(a,al2)<=angle and a!=al1 and a!=al2:
                return(True)
            return(False)            
    else:
        if strict=='false':
            if distanceAngle(a,al1)+distanceAngle(a,al2)>angle:
                return(True)
            return(False)
        else:
            if distanceAngle(a,al1)+distanceAngle(a,al2)>=angle and a!=al1 and a!=al2:
                return(True)
            return(False)
    #attention: pas assez de réflection consacrée à l'inégalité stricte ou non
    # l'arrondi machine peut provoquer des erreurs avec le strict...
    # avec le strict plus rien ne marche dans les cartes...normal car la méthode est 
    # plus précise que prévu: c'est soit une égalité soit une inégalité=en dehors