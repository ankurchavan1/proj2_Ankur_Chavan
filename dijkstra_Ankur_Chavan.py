# Ankur Mahesh Chavan
# achavan1@umd.edu

#Importing all the libraries
import numpy as np
import math
import heapq
import time
import cv2
import pygame


#moving up thorugh the coordinate points on the cartersian plane
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

def move_up(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0]
    new_node[1]=current_node[1] - 1
    cost=1
    return new_node,cost

def move_down(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0]
    new_node[1]=current_node[1] + 1
    cost=1
    return new_node,cost

def move_top_left(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0] - 1
    new_node[1]=current_node[1] - 1
    cost= 1.4
    return new_node,cost

def move_top_right(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0] + 1
    new_node[1]=current_node[1] - 1
    cost=1.4
    return new_node,cost

def move_bottom_left(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0] - 1
    new_node[1]=current_node[1] + 1
    cost=1.4
    return new_node,cost

def move_bottom_right(current_node):
    new_node=[0,0]
    new_node[0]=current_node[0] + 1
    new_node[1]=current_node[1] + 1
    cost=1.4
    return new_node,cost