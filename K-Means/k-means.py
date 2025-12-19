# k-means one-go

import math
import random
k=3
# list of k centroid points containing (x,y) coordinates: 
centroids=[]

# All data points from file in list format:
all_data_points=[]

# grouping of data_points to their nearest centroids
groups_dict={}
# Euclidean Distance:
def find_distance(centroid,point):
    # d = sqrt( ((x1-x2)^2) + ((y1-y2)^2) )
    d= math.sqrt( ((centroid[0]-point[0])*(centroid[0]-point[0])) + ((centroid[1]-point[1])*(centroid[1]-point[1])) )
    return d
# reading data from file and appending in all_data_points list
with open("clustering_data.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    parts = line.split(",")
    x = float(parts[0])
    y = float(parts[1])
    all_data_points.append([x, y])
# initializing first three centroids :
for i in range (0,3):
    centroids.append(all_data_points[i])

# Clustering Func
def clustering():
    # initializing empty lists of "k" groups :
    for i in range(k):
        groups_dict[i] = []
    
    # calculate dist of every point with all "k" centroids and group with minimum distanced centroid  
    for i in range (0,len(all_data_points)):
        distance_with_centroids=[]
        for j in range(0,len(centroids)):
            dist=find_distance(centroids[j],all_data_points[i])
            distance_with_centroids.append(dist)
        min_idx=distance_with_centroids.index(min(distance_with_centroids))
        groups_dict[min_idx].append(all_data_points[i])

# calculating Mean of each group 
def calc_mean_centroids(dict_groups):
    updated_centroids=[]
    for i in range (0, len(dict_groups)):
        x_mean=0
        y_mean=0
        list_of_points=dict_groups[i]
        for point in list_of_points:
            x_mean=x_mean+point[0]
            y_mean=y_mean+point[1]
        x_mean=x_mean/len(list_of_points)
        y_mean=y_mean/len(list_of_points)
        updated_centroids.append([x_mean, y_mean])
    return updated_centroids
# decide whether to continue finding new centroids or stop the process
def continue_process(prev_centroids,new_centroids):
    for i in range(0,len(prev_centroids)):
        dist=find_distance(prev_centroids[i],new_centroids[i])
        if (dist>0.001):
            return True
    return False
# display each cluster data points:
def display_Clusters(centroids,groups_dict):
    for i in range(0,len(centroids)):
        c=centroids[i]
        print(f"\nCentroid {i}: {c}")
        print("Points in cluster:")
        for point in groups_dict[i]:
            print(f"  {point}")

# continue repeating process until the averages(centroids) become nearly equal
while(True):
    clustering()
    updated_centroids=[]
    updated_centroids=calc_mean_centroids(groups_dict)
    if (continue_process(centroids,updated_centroids)==False):
        print("\nFinal Clusters:\n ")
        display_Clusters(centroids,groups_dict)
        break
    centroids = updated_centroids.copy()



