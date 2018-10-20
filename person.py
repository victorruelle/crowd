
from angles import getAngle
from descartes import distancePoints,intersectionCercle,distancePointsP
import numpy as np
from global_variables import rp,exits,Xi,Xs,Yi,Ys
import matplotlib.pyplot as plt
from walls import wall_points
from gen_functions import alea

class Person():
    "définir une personne dans la Piece"
    def __init__(self,x,y,theta=180,rayonPropre=rp,blocked=False,bloquant=-1):
        self.rayon=distancePoints([0,0],[x,y])
        self.angle=getAngle(x,y) # we use polar coordinates
        self.theta=theta*np.pi/180 # direction in which  person walks
        self.rayonPropre=rayonPropre # radius of a person
        self.blocked=blocked # can not move
        self.bloquant=bloquant # blocks someone 
    def disp(self,ax=0,color="blue",compression=None):
        if ax==0:
            plt.plot([self.x()],[self.y()],'bo')
            plt.arrow(self.x(),self.y(),self.dx(),self.dy(), linewidth="1",color="grey")
        else:
            if compression != None:
                fcolor = (compression,0,0,0.5)
            else:
                fcolor = (0,0,0,0)
            circle = plt.Circle((self.x(), self.y()), self.rayonPropre, edgecolor=color,facecolor = fcolor)
            ax.add_artist(circle)
    def x(self):
        return(self.rayon*np.cos(self.angle))
    def y(self):
        return(self.rayon*np.sin(self.angle))
    def dx(self):
        return(np.cos(self.theta))
    def dy(self):
        return(np.sin(self.theta))
    def position(self):
        return((self.x(),self.y()))
    def avancer(self,x):
        nx=self.x()+x*np.cos(self.theta)
        ny=self.y()+x*np.sin(self.theta)
        self.angle=getAngle(nx,ny)
        self.rayon=distancePoints([0,0],[nx,ny])
    def thetaDeg(self,thetaDeg):
        self.theta=thetaDeg*np.pi/180
    def shift(self,x,angle):
        #donner l'angle en degrés
        angle=angle*np.pi/180
        nx=self.x()+x*np.cos(self.theta-angle)
        ny=self.y()+x*np.sin(self.theta-angle)
        self.angle=getAngle(nx,ny)
        self.rayon=distancePoints([0,0],[nx,ny])
    def distance_to_exit(self):
        return(distancePoints((self.x(),self.y()),(0,0.5*(exits[0][0]+exits[0][1]))))

def init(N,obstacles):
    X,Y=[],[]
    Coordonnées = remplirCoordonnées(N,obstacles)
    for i in range(N):
        x,y = Coordonnées[i]
        p = Person(x,y)
        X.append( [ p , False ] ) # list of people and whether they have been evacuated
        Y.append( [ p.distance_to_exit() , i ] ) # shadow list to avoid computing the distance to exit everytime + info on original index
        calcAngle(X[i][0],obstacles)
    return X,Y 


def remplirCoordonnées(N,obstacles):
    Coordonnées = []
    while len(Coordonnées)<N:
        point=(alea(Xi,Xs),alea(Yi,Ys))
        if positionValide(Coordonnées,point,obstacles):
            Coordonnées.append(point)
    return Coordonnées

def positionValide(Coordonnées,point,obstacles) :
    for pt in Coordonnées:
        if distancePoints(pt,point) < 2*rp :
            return False
    for o in obstacles:
        if distancePoints(point,o[0])<=o[1]+rp:
            return False
    for points in wall_points:
        if distancePoints(points,point)<=rp*1.3:
            return False
    return True

def viserSortie(p):
    x,yi,ys= 0 , exits[0][0] , exits[0][1]
    if yi + p.rayonPropre <= p.y() <= ys - p.rayonPropre :
        p.thetaDeg(180)
    if p.y() > ys - p.rayonPropre:
        p.theta = getAngle( x - p.x() , ys - p.rayonPropre - p.y() )
    if p.y() < yi + p.rayonPropre:
        p.theta = getAngle( x - p.x() , yi + p.rayonPropre - p.y() )

def calcAngle(p,obstacles):
    viserSortie(p)
    dt,j=-1,0
    xp,yp=p.x(),p.y()
    O=[]
    for i in range(len(obstacles)):
        Test,Sol = intersectionCercle(p,i,obstacles)
        if Test:
            O.append([i,Sol])
    if len(O)==0:
        pass
    else:
        for i in range(len(O)):
            j,Sol=O[i]
            dt1,dt2 = distancePoints((xp,yp),Sol[1]) , distancePoints((xp,yp),Sol[1])
            if dt1<dt or dt2<dt or dt==-1 :
                dt=min(dt1,dt2)
                k=i
        l=O[k][0]
        xc,yc=obstacles[l][0]
        r=obstacles[l][1]
        dx,dy=xp-xc,yp-yc
        if distancePoints((xp,yp),(xc,yc))<=r+3*rp:
            if dx==0:
                p.thetaDeg(180)
            if dy<=0:
                p.theta=getAngle(dy,-dx)
            if dy>0:
                p.theta=getAngle(-dy,dx)
        else:
            dy = ( yc + r + rp - yp if yp>yc else yc - r - rp - yp)
            p.theta=getAngle(-dx,dy)


def invalid_movement(X,j,obstacles,test=1) :
    p=X[j][0]
    for i in range(len(X)):
        if i!=j and not(X[i][1]) and distancePoints(p.position(),X[i][0].position() ) < 2*rp :
            if test==1:            
                p.bloquant=i
            return True
    for o in obstacles:
        if distancePoints(p.position(),o[0])<=o[1]+rp:
            p.blocked=True
            return True
    for points in wall_points:
        if distancePoints(points,p.position())<=rp*1.3:
            return True
    return False

def compression(X,i):
    compte=0
    p=X[i][0]
    for j in range(len(X)):
        if j!=i:
            pt=X[j][0]
            if distancePointsP(p,pt)<=3*rp and pt.x()>0:
                compte+=1
    return(min(compte/5,1))