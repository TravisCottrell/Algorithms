import random
import math
import matplotlib.pyplot as plt

# 1.generate random centroids
# 2.get the distance from each point to each centroid and place them in the closest centroids cluster
# 3.move the centroid to the center of all the points of a cluster
# 4 repeat 2-3 as many times as requiired


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Kmeans:
    def __init__(self,numCentroids, shiftThreshold, radius , maxLoops, points):
        self.numCentroids = numCentroids
        self.shiftThreshold = shiftThreshold
        self.radius = radius
        self.maxLoops = maxLoops
        self.points = points
        self.centroids = []
        self.clusters = []
        self.outliers = []
        self.oldclusters = []
        
        
   
    def initialCentoids(self,min_graph, max_graph):
        
        for i in range(self.numCentroids):
            self.centroids.append(Point(random.randint(min_graph, max_graph),random.randint(min_graph, max_graph)))
            
        
    def clustering(self):
        self.clusters = [[]for _ in range(self.numCentroids)] 
        self.outliers = []
        
        #put points in the cluster with the closest centroid
        for point in self.points:
            centroidNo = 0
            lowestDistance = None
            for cent in self.centroids:
                distance = math.dist([point.x,point.y],[cent.x,cent.y])#euclidian distance of a point to the current coentroid
                
                if lowestDistance is None or distance < lowestDistance :
                    lowestDistance = distance
                    clusterNo = centroidNo
                centroidNo += 1
            if lowestDistance < self.radius:  
                self.clusters[clusterNo].append(point)
            else:
                self.outliers.append(point)
                
        for i, cent in enumerate(self.clusters):
            print(f"cluster:{i} ({self.centroids[i].x}, {self.centroids[i].y})")
            for point in cent:
                print(f"({point.x}, {point.y})")
                
        print("outliers:")
        for point in self.outliers:
            print(f"({point.x}, {point.y})")
                
    def adjustCentroids(self):
        for i, cluster in enumerate(self.clusters):
            clusterLength = len(cluster)
            print("cluster:",i)
            print("total points:", clusterLength)
            print(f"original centroid: ({self.centroids[i].x}, {self.centroids[i].y})")
            
            if clusterLength > 0:
                Xtotal = 0
                Ytotal = 0
                for point in cluster:
                    Xtotal += point.x
                    Ytotal += point.y
                    
                Xmean = round(Xtotal / clusterLength, 3)
                Ymean = round(Ytotal / clusterLength, 3)
                
                newCent = Point(Xmean,Ymean)
                distance = math.dist([self.centroids[i].x,self.centroids[i].y],[newCent.x,newCent.y])
                if distance > self.shiftThreshold:
                    self.centroids[i] = newCent
                else: 
                    print("didn't shift")
            print(f"new centroid: ({self.centroids[i].x}, {self.centroids[i].y})\n")
        
