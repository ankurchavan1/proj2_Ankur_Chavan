# Ankur Mahesh Chavan
# achavan1@umd.edu

import pygame
import math
import sys
import numpy as np




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
