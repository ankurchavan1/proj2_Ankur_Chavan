# Ankur Mahesh Chavan
# achavan1@umd.edu

import pygame
import math
import sys
import numpy as np

# defining the obstacle space using half equations
def obstacle_space(x,y):
    obs_present = 0
    if (x <= 5) and (x >= 595) and (y <=5) and (y >= 245):
        obs_present=1
    if x >= 95 and x <= 155 and y>= 145 and y <= 255:
        obs_present=1
    if (x >= 95) and (x <= 155) and (y>=0) and (y <= 105):
        obs_present=1
    if x >= 230.05 and x <= 369.95 and (((y - 165.38) - ((165.38 - 205.77)/ (230.05 - 300))* (x - 230.05)) <= 0) and (((y - 205.77) - ((205.77 - 165.38)/(300 - 369.95))* (x - 300)) <= 0) and (((y - 84.61) - ((84.61 - 44.22)/ (369.95 - 300))* (x - 369.95)) >= 0) and (((y - 44.22) - ((44.22 - 84.61)/ (300 - 230.04))* (x - 300)) >= 0):
        obs_present=1
    if x>= 455 and (((y - 246.18) - ((246.18 - 125)/ (455 - 515.59))*(x - 455)) <= 0) and (((y - 125) - ((125 - 3.81)/ (515.19 - 455))*(x - 515.59)) >= 0):
        obs_present=1
    return obs_present

# taking input from the user
print("Enter start node cordinates")

x_of_start_node=float(input("Enter the x coordinate of start node:"))
y_of_start_node=float(input("Enter the y coordinate of start node:"))
start_node=[x_of_start_node, y_of_start_node]

print("Enter goal node cordinates")
x_of_goal_node=float(input("Enter the x coordinate of goal node:"))
y_of_goal_node=float(input("Enter the y coordinate of goal node:"))
goal_node=[x_of_goal_node,y_of_goal_node]


rows=250
coloums=600

# Function for all 8 movements
def move_left(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0]-1
    new_node[1]=current_node[1]
    cost=1
    return new_node,cost

def move_right(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0]+1
    new_node[1]=current_node[1]
    cost=1
    return new_node,cost

def move_down(cureent_node):
    new_node=[0,0]
    new_node[0]=cureent_node[0]
    new_node[1]=cureent_node[1]+1
    cost=1
    return new_node,cost

def move_up(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0]
    new_node[1]=current_node[1]-1
    cost=1
    return new_node,cost

def move_bottom_left(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0]-1
    new_node[1]=current_node[1]+1
    cost=1.42
    return new_node,cost

def move_top_left(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0]-1
    new_node[1]=current_node[1]-1
    cost=1.42
    return new_node,cost
                  
def move_top_right(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0]+1
    new_node[1]=current_node[1]-1
    cost=1.42
    return new_node,cost
                  
def move_bottom_right(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0]+1
    new_node[1]=current_node[1]+1
    cost=1.42
    return new_node,cost

# Dijkstra Implementation
parent_node=[start_node]
candidate_nodes=[start_node]
list_of_parent_nodes=[]
list_of_visited_nodes=[]
costs_list=[]

# Checking the validity of the allowed start and goal nodes
if (obstacle_space(goal_node[0],goal_node[1])==1 or obstacle_space(start_node[0],start_node[1])):
    sys.exit("Goal Node or start node lies within obstackle space, please enter valid nodes")

if (start_node[0] not in range(0,601) or goal_node[0] not in range(0,601) or start_node[1] not in range(0,251) or goal_node[1] not in range(0,251)):
    sys.exit("Goal node or start node not within the allowed boundary limits")

x=0
cost_i=[0]
node=start_node
flag=0

# While loop
while(flag!=1 and candidate_nodes!=[]):
    
    # Up action
    new_nd,cost=move_up(node)
    if (new_nd[1]>=0 and obstacle_space(new_nd[0],new_nd[1])!=1):
        if new_nd not in list_of_visited_nodes:
            indices_lst=range(0,len(candidate_nodes))
            indices_lst=indices_lst[::-1]
            check=0
            for index_i in indices_lst:
                if(new_nd == candidate_nodes[index_i]):
                    check=1
                    if(cost_i[index_i]>=(cost_i[x]+cost)):
                        parent_node[index_i]=node
                        cost_i[index_i]=round((cost_i[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                parent_node.append(node)
                candidate_nodes.append(new_nd)
                cost_i.append(round((cost+cost_i[x]),1))
            
            
    # down action
    new_nd,cost=move_down(node)
    if (new_nd[1]<=rows and obstacle_space(new_nd[0],new_nd[1])!=1):
        if new_nd not in list_of_visited_nodes:
            indices_lst=range(0,len(candidate_nodes))
            indices_lst=indices_lst[::-1]
            check=0
            for index_i in indices_lst:
                if(new_nd == candidate_nodes[index_i]):
                    check=1
                    if(cost_i[index_i]>=(cost_i[x]+cost)):
                        parent_node[index_i]=node
                        cost_i[index_i]=round((cost_i[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                parent_node.append(node)
                candidate_nodes.append(new_nd)
                cost_i.append(round((cost+cost_i[x]),1))
            

            
    # left action
    new_nd,cost=move_left(node)
    if (new_nd[0]>=0 and obstacle_space(new_nd[0],new_nd[1])!=1):
        if new_nd not in list_of_visited_nodes:
            indices_lst=range(0,len(candidate_nodes))
            indices_lst=indices_lst[::-1]
            check=0
            for index_i in indices_lst:
                if(new_nd == candidate_nodes[index_i]):
                    check=1
                    if(cost_i[index_i]>=(cost_i[x]+cost)):
                        parent_node[index_i]=node
                        cost_i[index_i]=round((cost_i[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                parent_node.append(node)
                candidate_nodes.append(new_nd)
                cost_i.append(round((cost+cost_i[x]),1))

                                  
                
    # right action
    new_nd,cost=move_right(node)
    if (new_nd[0]<=coloums and obstacle_space(new_nd[0],new_nd[1])!=1):
        if new_nd not in list_of_visited_nodes:
            indices_lst=range(0,len(candidate_nodes))
            indices_lst=indices_lst[::-1]
            check=0
            for index_i in indices_lst:
                if(new_nd == candidate_nodes[index_i]):
                    check=1
                    if(cost_i[index_i]>=(cost_i[x]+cost)):
                        parent_node[index_i]=node
                        cost_i[index_i]=round((cost_i[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                parent_node.append(node)
                candidate_nodes.append(new_nd)
                cost_i.append(round((cost+cost_i[x]),1))

             
    # top left action
    new_nd,cost=move_top_left(node)
    if (new_nd[1]>=0 and new_nd[0]>=0 and obstacle_space(new_nd[0],new_nd[1])!=1):
        if new_nd not in list_of_visited_nodes:
            indices_lst=range(0,len(candidate_nodes))
            indices_lst=indices_lst[::-1]
            check=0
            for index_i in indices_lst:
                if(new_nd == candidate_nodes[index_i]):
                    check=1
                    if(cost_i[index_i]>=(cost_i[x]+cost)):
                        parent_node[index_i]=node
                        cost_i[index_i]=round((cost_i[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                parent_node.append(node)
                candidate_nodes.append(new_nd)
                cost_i.append(round((cost+cost_i[x]),1))

            
    # top right action
    new_nd,cost=move_top_right(node)
    if (new_nd[0]<=coloums and new_nd[1]>=0 and obstacle_space(new_nd[0],new_nd[1])!=1):
        if new_nd not in list_of_visited_nodes:
            indices_lst=range(0,len(candidate_nodes))
            indices_lst=indices_lst[::-1]
            check=0
            for index_i in indices_lst:
                if(new_nd == candidate_nodes[index_i]):
                    check=1
                    if(cost_i[index_i]>=(cost_i[x]+cost)):
                        parent_node[index_i]=node
                        cost_i[index_i]=round((cost_i[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                parent_node.append(node)
                candidate_nodes.append(new_nd)
                cost_i.append(round((cost+cost_i[x]),1))

            
    # bottom left action
    new_nd,cost=move_bottom_left(node)
    if (new_nd[1]<=rows and new_nd[0]>=0 and obstacle_space(new_nd[0],new_nd[1])!=1):
        if new_nd not in list_of_visited_nodes:
            indices_lst=range(0,len(candidate_nodes))
            indices_lst=indices_lst[::-1]
            check=0
            for index_i in indices_lst:
                if(new_nd == candidate_nodes[index_i]):
                    check=1
                    if(cost_i[index_i]>=(cost_i[x]+cost)):
                        parent_node[index_i]=node
                        cost_i[index_i]=round((cost_i[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                parent_node.append(node)
                candidate_nodes.append(new_nd)
                cost_i.append(round((cost+cost_i[x]),1))

            
    # bottom right action
    new_nd,cost=move_bottom_right(node)
    if (new_nd[1]<=rows and new_nd[0]<=coloums and obstacle_space(new_nd[0],new_nd[1])!=1):
        if new_nd not in list_of_visited_nodes:
            indices_lst=range(0,len(candidate_nodes))
            indices_lst=indices_lst[::-1]
            check=0
            for index_i in indices_lst:
                if(new_nd == candidate_nodes[index_i]):
                    check=1
                    if(cost_i[index_i]>=(cost_i[x]+cost)):
                        parent_node[index_i]=node
                        cost_i[index_i]=round((cost_i[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                parent_node.append(node)
                candidate_nodes.append(new_nd)
                cost_i.append(round((cost+cost_i[x]),1))

    # Appending all the lists      
    list_of_parent_nodes.append(parent_node.pop(x))
    list_of_visited_nodes.append(candidate_nodes.pop(x))
    costs_list.append(cost_i.pop(x))
    
    if(list_of_visited_nodes[-1]==goal_node):
        flag=1
        
    if(flag!=1 and candidate_nodes!=[]):
        x=cost_i.index(min(cost_i))
        node=candidate_nodes[x][:]
    
if(flag==0 and candidate_nodes==[]):
    sys.exit("Path does not exist")
    
# Final Path
path=[]
path.append(list_of_visited_nodes[-1])
path.append(list_of_parent_nodes[-1])
x=list_of_parent_nodes[-1]
i=1
while(x!=start_node):
    if(list_of_visited_nodes[-i]==x):
        path.append(list_of_parent_nodes[-i])
        x=list_of_parent_nodes[-i]
    i=i+1      


obstacle_grid = []
for i in range(0,601):
    for j in range(0,251):
        q=obstacle_space(i,j)
        if q == 1:
            obstacle_grid.append([i,j])

scale_factor=2
vn_list = np.array(list_of_visited_nodes)
list_of_visited_nodes=vn_list*scale_factor
path_array = np.array(path)
path=path_array*scale_factor
obstacle_grid_array = np.array(obstacle_grid)
obstacle_grid = obstacle_grid_array*scale_factor

# Visualization
pygame.init()

# Colors
Black = [0, 0, 0]
Red = [255, 0, 0]
Blue = [0, 100, 255]
White = [255, 255, 255]
Green = [0, 255, 0]

# Grid
SIZE = [600*scale_factor, 250*scale_factor]
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Result: Path finding using Dijkstra")
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            done = True   
 
    screen.fill(Black)
# Grid
    for i in obstacle_grid:
        pygame.draw.rect(screen, White, [i[0],250*scale_factor-i[1],scale_factor,scale_factor])
    pygame.display.flip()
    clock.tick(20)
# Visited Nodes
    for i in list_of_visited_nodes:
        pygame.time.wait(1)
        pygame.draw.rect(screen, Green, [i[0],250*scale_factor-i[1],scale_factor,scale_factor])
        pygame.display.flip()
# Path
    for j in path[::-1]:
        pygame.time.wait(1)
        pygame.draw.rect(screen, Red, [j[0], 250*scale_factor-j[1], scale_factor,scale_factor])
        pygame.display.flip()
    pygame.display.flip()

    pygame.time.wait(3000)
    done = True
pygame.quit()
