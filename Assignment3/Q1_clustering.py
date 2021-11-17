#!/usr/bin/env python
# coding: utf-8

# -*- coding: utf-8 -*-
"""
CS 351 - Artificial Intelligence 
Assignment 3

Student 1(Name and ID):
Student 2(Name and ID):

"""
import math
# from math import pi
import random
from matplotlib.colors import cnames
import numpy as np
import matplotlib.pyplot as plt


def initializePoints(count):
    points = []
    for i in range(int(count/3)):
        points.append([random.gauss(0,10),random.gauss(100,10)])
    for i in range(int(count/3)):
        points.append([random.gauss(-30,20),random.gauss(10,10)])
    for i in range(int(count/3)):
        points.append([random.gauss(30,20),random.gauss(10,10)])

    return points

def check():
    pass

def euc_dist(point, centroid):
    return(math.sqrt((point[0] - centroid[0])**2 + (point[1] - centroid[1])**2 ))

def cluster(points,K,visuals = True):
    clusters=[]

    #Your kmeans code will go here to cluster given points in K clsuters. If visuals = True, the code will also plot graphs to show the current state of clustering
    
    centroids = dict()
    past_centroids = dict()
    
    iterations = 0
    if (iterations == 0):
        for i in range(K):
            temp = points[random.randrange(0, len(points))]
            centroids[(temp[0], temp[1])] = []
        
    
    # generating centroids (cluster centers)
    # cluster
    check = 0
    while(check <= 2): #check() != True):
        if (iterations != 0):
            past_centroids = centroids
            centroids = dict()
            for key in past_centroids:
                # get all x, y
                x = []
                y = []
                point_lst = past_centroids[key]
                for i in range(len(point_lst)):
                    x.append(point_lst[i][0])
                    y.append(point_lst[i][1])

                # print(list(zip(past_centroids[key]))[0][0])
                # mean_x = sum(list(zip(past_centroids[key]))[0][0]) / len(past_centroids[key])
                # mean_y = sum(list(zip(past_centroids[key]))[1][0]) / len(past_centroids[key])
                mean_x = sum(x) / len(x)
                mean_y = sum(y) / len(y)
                centroids[(mean_x, mean_y)] = []

        for point in range(len(points)):
            # print(point)
            min_dist = math.inf
            choosen_center = list(centroids.keys())[0] # randomly choosing first centroid
            for each_centroid in centroids:
                # print(each_centroid)
                curr_dist = euc_dist(points[point], each_centroid)
                if(curr_dist < min_dist):
                    choosen_center = each_centroid
                    min_dist = curr_dist
            centroids[choosen_center].append(points[point])

        iterations += 1

        # plotting
        clr = ['red','green','blue']
        i = 0
        for centroid in centroids:
            # print(centroid)
            lst = centroids[centroid]
            # print("lst = ", lst)
            if(len(lst) != 0):
                x, y = zip(*lst)
                plt.scatter(x,y , color=clr[i])
                i += 1
            plt.scatter(centroid[0], centroid[1], color='black')

        plt.show()
        
        check += 1
    # x, y = zip(*points)

    # x = np.random.rand(N)
    # y = np.random.rand(N)

    # plt.scatter(x, y)


    
    return clusters



def clusterQuality(clusters):
    score = -1
    #Your code to compute the quality of cluster will go here.
    
    return score
    

def keepClustering(points,K,N,visuals):
    clusters = []
    
    #Write you code to run clustering N times and return the formation having the best quality. 
    for n in range(N):
        cluster(points, K, False)
        break
    
    return clusters
    



K = 3
N = 10
points = initializePoints(1000)



clusters = keepClustering(points,K,N,True)

print ("The score of best Kmeans clustering is:", clusterQuality(clusters))
