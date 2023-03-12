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


print("Enter robot parameters")
rad=float(input("radius =  "))
clr=float(input("clearence =  "))

print("Enter initial node cordinates")

x_of_start_node=float(input("Enter the x coordinate of start node:"))
y_of_start_node=float(input("Enter the y coordinate of start node"))
start_node=[x_of_start_node, y_of_start_node]

print("Enter goal node cordinates")
x_of_goal_node=float(input("Enter the x coordinate of goal node:"))
y_of_goal_node=float(input("Enter the y coordinate of goal node:"))
goal_node=[x_of_goal_node,y_of_goal_node]
# r=int(input("Enter Resolution (must be an integer value) =  "))

# goal_node= [n / r for n in goal_node]
# start_node=[m / r for m in start_node]

rows=150

coloums=250



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
