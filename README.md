# ENPM661 Project 2: Implementation of Dijkstra Algorithm

This repository contains the implementation of Dijkstra Algorithm for path planning in a 2D grid environment with obstacles. 
The code takes the start node and goal node positions as input from the user and provides the visual representation of all the node exploration while avoiding the obstacles. In the end, it shows the shortest path from start to goal node.

# Libraries Used
1. pygame
2. math
3. sys
4. numpy

# Usage
Clone the repository on your local machine.
Open the terminal and navigate to the repository directory.
Run the command python main.py to start the program.
Input the x and y coordinates of the start node and goal node as prompted.
The program will display the visualization of the exploration of all the nodes in the environment while avoiding obstacles.
Once the exploration is complete, the shortest path from start to goal node will be displayed.
Close the window to terminate the program.

# Note
While calculating the obstacle space, the clearance value has been hard-coded while defining the obstacle space itself. 
To make it more modular, the ideal way is to take the clearance as a variable and incorporate it into the half equations.
