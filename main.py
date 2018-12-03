from crowd_evacuation import simulation
from global_variables import obstacles

N = 50
try:
    N = int(input("how many people in the simulation? "))
except ValueError:
    print("invalid entry, using N =",N,"instead")

save = True if input("do you want to save images showing the evac ? (y/n) ") == "y" else False

time,no_blocked = simulation(N,obstacles,save=save)

print("the evacuation took",time,"timesteps, leaving",no_blocked,"people dead")