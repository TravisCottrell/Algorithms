import matplotlib.pyplot as plt
import random
import numpy as np

from Kmeans import Kmeans, Point


totalPoints = 200
numberOfCentroids = 5
maxLoops = 6
shiftThreshold = np.finfo(float).eps 
radius = 30

min_graph = -100
max_graph = 100

points = []
#completely random points that are unique to each other
i = 0
while i < totalPoints:
    temppoint = Point(random.randint(min_graph, max_graph),random.randint(min_graph, max_graph))
    if len(points) <= 0:
         points.append(temppoint)
    check = False
    for point in points:
        if point.x == temppoint.x and point.y == temppoint.y:
            check = True
            
    if check == False:   
        points.append(temppoint)
        i += 1
loopcheck = True
while loopcheck:
    km = Kmeans(numberOfCentroids, shiftThreshold, radius, maxLoops, points)
    km.initialCentoids(min_graph, max_graph)
    totalLoops = 0
    while totalLoops < maxLoops:
        km.clustering()
        print("----------------------------------------------------")
        print("adjustment:", totalLoops)
        km.adjustCentroids()
        print("end adjustment: ", totalLoops)
        print("----------------------------------------------------")
        totalLoops += 1

    plt.figure(figsize=(8, 8))

    circles = []
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    for i, cent in enumerate(km.clusters):
        circles.append(plt.Circle((km.centroids[i].x, km.centroids[i].y), radius, fill=False, edgecolor=colors[i]))
        for point in cent:
            plt.scatter(point.x, point.y, color = colors[i])
            

    for point in km.outliers:
        plt.scatter(point.x, point.y, color = "black")
        

    fig = plt.gcf()
    ax = fig.gca()
    for circle in circles:
        ax.add_patch(circle)

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.xlim([min_graph, max_graph])
    plt.ylim([min_graph, max_graph])
    plt.show()
    check = input("run again? y or n")
    if check == 'n': loopcheck = False