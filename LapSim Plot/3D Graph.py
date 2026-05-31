import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
from scipy.interpolate import RegularGridInterpolator as rgi

from CSV_Scraper import Scraper


### INTERPOLATION ###

#Interpolates point based on Cd + Cl values
def interpolate(cd_axis, cl_axis, Z):
    
    #fxn takes 2 arguments so make tuplet
    points = (cd_axis, cl_axis)
    
    #fxn maps given cd/cl to corresponding Z
    #note: extrapolation possible, but less accurate for Cd > 4 and Cl > 6
    fxn = rgi(points, Z.T, bounds_error = False, fill_value = None)

    cdInput = float(input("What is your Cd value?\n"))
    clInput = float(input("What is your Cl value?\n"))
    
    #fxn needs 1 argument, so make vals 1 matrix instead of 2 lists
    vals = [[cdInput, clInput]]
    
    result = fxn(vals)
    print("\nInterpolated value is:", result[0])
    
    #plot interpolated point
    ax.scatter(cdInput, clInput, result[0], color='black', s=50, marker='*')
    
    
   
 ### GRAPHING ###   
    
#creates 3D plot of specified event
def graph(X, Y, ac, sk, au, en, tot):
    
    track = None
        
    #prompt
    print("\nWhich points graph would you like to display?\n")
    print("1. Acceleration\n2. Skidpad\n3. Autocross\n4. Endurance")
    print("5. Total Points\n")
    graph_choice = int(input())

    #elif elif elif
    if(graph_choice == 1):
        track = ac
    elif(graph_choice == 2):
        track = sk
    elif(graph_choice == 3):
        track = au
    elif(graph_choice == 4):
        track = en
    elif(graph_choice == 5):
        track = tot

    
    #reshape track (currently 1d array) to correct size
    Z = track.values.reshape(21,21).T
    
    # Normalize to [0,1] for colour mapping
    norm = plt.Normalize(Z.min(), Z.max())
    colours = cm.viridis(norm(Z))
    
    #colours is 3D with rows, columns and colour, so must use '_' to match dimensions
    rows, columns, _ = colours.shape

    #mesh grid plot
    surf = ax.plot_surface(X, Y, Z, rcount=rows, ccount=columns,
                        facecolors=colours, shade=False)
    surf.set_facecolor((0,0,0,0))
    
    return Z



### OVERLAY ###

#overlays 3D plots of all 4 events (surface map)
def graph_overlay(X, Y, ac, sk, au, en, tot):
    ax.plot_surface(X, Y, ac.values.reshape(21,21).T, cmap="Blues", label='Acceleration')
    ax.plot_surface(X, Y, sk.values.reshape(21,21).T, cmap="Grays", label='Skidpad')
    ax.plot_surface(X, Y, au.values.reshape(21,21).T, cmap="Reds", label='Autocross')
    ax.plot_surface(X, Y, en.values.reshape(21,21).T, cmap="Greens", label='Endurance')
    ax.legend()



### MAIN ###

#import from scraper
data = Scraper()

data.parse()
ac = data.getAc()
sk = data.getSk()
au = data.getAu()
en = data.getEn()
tot = data.getTot()

#surface plot
ax = plt.axes(projection="3d")


#cd + cl increments, make meshgrid
cd = np.arange(0, 4.2, 0.2)
cl = np.arange(0, 6.3, 0.3)
X, Y = np.meshgrid(cd, cl)


#choose whether to overlay graphs or pick a single one
print("\nSingle Graph (1) or Graph Overlay (2)?\n")
num = int(input())

if(num == 1):
    Z = graph(X, Y, ac, sk, au, en, tot)
    
    #comment interpolate fxn call if not wanted
    interpolate(cd,cl,Z)

else:
    graph_overlay(X, Y, ac, sk, au, en, tot)


#plot!
ax.set_xlabel('Cd')
ax.set_ylabel('Cl')
ax.set_zlabel('Points')

plt.show()