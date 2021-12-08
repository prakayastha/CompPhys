import numpy as np
import matplotlib.pyplot as plt

print("Initialising the simulation...")

# define function that describe the Lorenz system.
def Lorenz(sigma,r,b,xyz):
    
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    
    fx = sigma*(y-x)
    fy = (r*x)-y-(x*z)
    fz = (x*y)-(b*z)
    
    return np.array([fx,fy,fz],float)

# Simulation parameters
start = 0                  # start time
end = 50                 # end time
num_steps = 3000         # number of time steps
h = (end-start) / num_steps  # time step size

# intitial conditions: x=0, y=1, z=0
xyz = np.array([0,1,0],float)

# constants
sigma = 10
r = 28
b = 8/3

# generate times at which to evaluate xyz
time_list = np.arange(start,end,h)

# create empty arrays to hold the calculated values
x_points = []
y_points = []
z_points = []

print("Applying Euler's method...")

# Apply Euler's method
for time in time_list:
    
    x_points.append(xyz[0])
    y_points.append(xyz[1])
    z_points.append(xyz[2])
    xyz += h*Lorenz(sigma,r,b,xyz)
    
print("Plotting the results...")

# Plot the strange attractor
plt.plot(x_points,z_points)
plt.savefig("Strange_attractor.png")
