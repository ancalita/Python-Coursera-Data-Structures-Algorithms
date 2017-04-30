import math
import heapq


def minimum_distance(n, x, y):
    
    result = 0
    cost = {};
    h = [];
    vertices = {}
    new_tree = {}
    
    for i in range(n):
        if i == 0:
            cost[i] = 0;
        else:
            cost[i] = float('inf');
        heapq.heappush(h, (cost[i],i));
        vertices[i] = i;
    
    while len(h)>0:
        (c, v) = heapq.heappop(h);
        del vertices[v]
        new_tree[v]=v;
        edge_weights = [];
        for vertex in vertices.values():
            for existent in new_tree.values():
                w = math.sqrt((x[existent]-x[vertex])**2 + (y[existent]-y[vertex])**2);
                heapq.heappush(edge_weights,(w, vertex));
        if len(edge_weights)>0:
            (min_w, z) = heapq.heappop(edge_weights);
            if cost[z] > min_w:
                cost[z] = min_w;
                result+= min_w;
                new_list=[];
                for (weight, node) in h:
                    if node == z:
                        new_list.append((min_w, z))
                    else:
                        new_list.append((weight, node))
                h = new_list;
                heapq.heapify(h);   
    return result

x = [0,0,1,3,3]
y = [0,2,1,0,2]
print("{0:.9f}".format(minimum_distance(5, x, y)))