import random

#Clustering was implemented as one of the methods for application in secondary search.
#The number of groups to be clustered and the entire element is entered.
def Clustering(list, k):
    if len(list)>=k:
        Cluster= [set('') for i in range (k)]
        total_idx=0
        while True:
            temp_cluster= [[] for i in range (k)]
            #Select as many random points as k and set them as centroid.
            centroid = random.sample(list, k)
            #Divide a set of points based on their distance from the centroid.
            for i in range (k):
                temp_cluster[i].append(centroid[i])
            for i in range (len(list)):
                if list[i] in centroid:
                    continue
                idx= 0
                dist= Find_dist(temp_cluster[0][0], list[i])
                for j in range (k-1):
                    if dist>Find_dist(temp_cluster[j+1][0], list[i]):
                        idx= j+1
                        dist= Find_dist(temp_cluster[j+1][0], list[i])
                temp_cluster[idx].append(list[i])

            temp_cluster_set= [set(temp_cluster[i]) for i in range (k)]
            for i in range (len(temp_cluster_set)):
                if temp_cluster_set[i] in Cluster:
                    total_idx+= 1
                else:
                    total_idx= 50
                    break

            total_idx-= len(temp_cluster_set)

            #After saving the results, return the values if they are the same as the results of the previous trial.
            Cluster = temp_cluster_set
            if total_idx < (50-len(temp_cluster_set)):
                total_idx+= 1
                if total_idx==2:
                    print(Cluster)
                    break
            else:
                total_idx=0


#It is a function that finds distance.
#At this time, the distance does not use Euclidean space.
#Because the RGB value is an integer only, the sum of the differences in each value is set as the distance.
def Find_dist(elem1, elem2):
    return abs(elem1[0]-elem2[0])+abs(elem1[1]-elem2[1])+abs(elem1[2]-elem2[2])

