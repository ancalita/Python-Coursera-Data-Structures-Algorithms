import math
import heapq

def clustering(n, x, y, k):

    result = 0;
    
    subsets = [[i] for i in range(n)]
    d_2 = [[] for i in range(n)]
    adj = [set() for i in range(n)]
    
    distances = [];
    for j in range(n):
        for l in range(n):
            if j!=l and (j not in adj[l]):
                d = math.sqrt((x[j]-x[l])**2 + (y[j]-y[l])**2);
                heapq.heappush(distances,(d, (j,l)));
                adj[j].add(l);
    
    total_distances = len(distances)
    edges_ordered = [heapq.heappop(distances) for e in range(total_distances)]
    
    def find(node, subset):
        for i in range(len(subset)):
            if node in subset[i]:
                return i;
                break
    
    def union(a,b,d, subset, dist_class):
        length = len(subset)
        for i in range(length):
            if a in subset[i]:
                for j in range(length):
                    if i!=j and b in subset[j]:
                        for e in subset[j]:
                            subset[i].append(e);
                            dist_class[i].append(d);
                        del subset[j]
                        break 
                break      
    
    for (d,(a,b)) in edges_ordered:
        idx_a = find(a, subsets);
        idx_b = find(b, subsets);
        if idx_a!=idx_b and len(subsets)>=k:
            union(a,b,d, subsets, d_2);
            if d>=max(d_2[idx_a]):
                result = d;
        else:
            d_2[idx_a].append(d);
                
    
    return result

#x = [7,4,5,1,2,5,3,7,2,4,6,2]
#y=[6,3,1,7,7,7,3,8,8,4,7,6]
#n=12
#k=3

x=[3,1,4,9,9,8,3,4]
y=[1,2,6,8,9,9,11,12]
n=8
k=4

print("{0:.9f}".format(clustering(n, x, y,k)))