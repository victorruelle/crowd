from global_variables import step
from person import invalid_movement

def unblock(X,obstacles):
    bloquagesMutuels=[]
    File=[]
    n=len(X)
    for i in range(n):
        p , fini = X[i]
        if fini:
            break
        if p.blocked : 
            j = p.bloquant
            p2, fini2 = X[j]
            if p2.blocked and p2.bloquant==i:
                bloquagesMutuels.append( [i,j] )
                File.append( i )
    for i in range(n):
        p , fini = X[i]
        if p.blocked and p.bloquant in File:
            File.append(i)
    triFile(X,File)
    for i in File:
        if evasion(X,obstacles,i):
            break
    
def triFile(X,File):
    Liste=[]
    n=len(File)
    for i in range(n):
        Liste.append( [ X[File[i]][0].distance_to_exit(), i ] )
    Liste.sort()
    FileC=File.copy()
    for i in range(n):
        File[i]=FileC[ Liste[i][1] ]
    del(FileC)


def evasion(X,obstacles,i):
    p, fini = X[i]
    angle=p.theta
    Angles = [ 45 , -45 , 90 , -90 ]
    for a in Angles:
        p.shift(step,angle+a)
        if not(invalid_movement(X,i,obstacles,test=0)):
            p.blocked=False
            return(True)
        p.shift(-step,angle+a)
    p.blocked=True
    return(False)