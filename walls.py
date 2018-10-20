from global_variables import rp,walls

def listeMurs(Murs):
    #computes the given walls in the right format
    Points=[]
    for segment in Murs:
        xi,xs,yi,ys= segment[0][0], segment[1][0] , segment[0][1] , segment[1][1]
        if xi==xs:
            pas=rp
            n=int((ys-yi)/pas)
            for i in range(n):
                Points.append([xi,yi+i*pas])
            Points.append([xi,ys])
        elif yi==ys:
            pas=rp
            n=int((xs-xi)/pas)
            for i in range(n):
                Points.append([xi+i*pas,yi])
            Points.append([xs,yi])
    return(Points) 

wall_points=listeMurs(walls)        
