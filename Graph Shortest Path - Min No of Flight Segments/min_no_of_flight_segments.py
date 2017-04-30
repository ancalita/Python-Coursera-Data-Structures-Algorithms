import Queue

def distance(a, s, t):

    frontier = Queue.Queue()
    frontier.put(s)
    dist = {};
    for i in range(len(adj)):
        dist[i]= float("inf")
    dist[s] = 0;
    
    while not frontier.empty():
        u = frontier.get()
        if u==t:
            return dist[u];
        else:
            neighbours=a[u];
            for e in neighbours:
                if dist[e] == float("inf"):
                    frontier.put(e);
                    dist[e] = dist[u] + 1;
    
    return -1

adj=[[1,3,2],[0,2],[1,0],[0]]
print(distance(adj,1,3))

adj_2= [[2,3],[4],[0,3],[2,0],[1]]
print(distance(adj_2, 3, 5))