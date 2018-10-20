
# GLOBAL VARIABLES
rp=0.1 # radius of a person
step=0.05 # length of a step
walls = [[(9, -1), (9, 8)], #bounds of the room
 [(0, -1), (0, 2.85)],
 [(0, 4.15), (0, 8)],
 [(0, -1), (9, -1)],
 [(0, 8), (9, 8)]]
Xi,Xs,Yi,Ys = 0.5 , 8.8 , -0.8 , 7.8 # spawning bounds for a person
exits = [[2.85,4.15]] # position of the exit on the left wall

#know obstacles
obstacles = [ [ (5,5.5) , 0.7] , [ (5,2.5) , 0.7 ] , [ (2,4.5) , 0.5 ] ] # a disposition of obstacles defined a a circle ((x,y),radius)
empty = [ ]
Obs1 = [ [ (4.5,5) , 0.7] , [ (4.5,2.5) , 0.7 ] ]
Obs2 = [ [ (4.5,3.5) , 2 ] ]
Obs3 = [ [ (3,3.5) , 0.7 ] , [ (5.5,2.3) , 0.7 ] , [ (5.5,4.8) , 0.7 ] ]

# in the room : x lives in [0,9] y in [-1,8]
