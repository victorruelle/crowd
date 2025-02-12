# Crowd movement modelling

This project was developped in my second year of undergraduate studies. It models the movement of a crowd of people (seen as circles) inside a rectangular room. 
I attempted to simulate an evacuation with a single exit and any number of circular obstacles. 

# How it works

The model that was developped relies solely on hand-written rules. 
People alway go directly for the exit except when an obstacle lies between them and their objective ; in that case they will naturally move around it.
The most complex part of the model lies in the resolution of obstructions : people tend to get stuck and must have strategies to move around the poeple that are blocking them.


# Results 

Several results have been added:
- an example of evacuation and the associated gif in the "output" folder
- an example of the evolution of the "heatmap" in the room during an evacuation
- an example of curves that can be obtained (here : time of evacuation / number of people for different type of obstacles)

![view of a sample evacuation](output/sample evacuation.gif?raw=true "Title")
    
# How to use 

Calling main.py will launch a simple evacuation where you will be asked to specify the number of people and choose if you want to save the images of each time step (this slows the process down by a lot!)
To change the obstacles, you will need to manually change those that are loaded by main.py ; there are 5 set of pre-coded obstacles that can be loaded from global_variables.py
Most varialbes (raidus of a person, length of a step, room size etc.) can be changed in global_variables.py

# Pending improvements
- too many people aim for the exact same point in the exit (to very bottom and very top of the exit); this leads to very unoptimal endings. Aimed exit point should be a continuous fonction on the angle between the midpoint of the exit and the person's coordoniates
- axis limits of saved images do not scale with the size of the room ; simple fix waiting