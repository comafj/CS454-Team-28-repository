import random


def Clustering(list, k):
    if len(list)>=k:
        Cluster= [set('') for i in range (k)]
        total_idx=0
        while True:
            temp_cluster= [[] for i in range (k)]
            centriod = random.sample(list, k)
            for i in range (k):
                temp_cluster[i].append(centriod[i])
            for i in range (len(list)):
                if list[i] in centriod:
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

            Cluster = temp_cluster_set
            if total_idx < (50-len(temp_cluster_set)):
                total_idx+= 1
                if total_idx==2:
                    print(Cluster)
                    break
            else:

                total_idx=0



def Find_dist(elem1, elem2):
    return abs(elem1[0]-elem2[0])+abs(elem1[1]-elem2[1])+abs(elem1[2]-elem2[2])



#cnd_elem = [(1,1,1),(1,2,1),(5,1,1),(12,1,41),(1,12,1),(1,15,1),(1,1,2),(8,2,1),(7,2,4)]
#cnd_elem = [(1,1,1),(1,2,1),(5,1,1),(12,1,41)]
#Clustering(cnd_elem, 2)

