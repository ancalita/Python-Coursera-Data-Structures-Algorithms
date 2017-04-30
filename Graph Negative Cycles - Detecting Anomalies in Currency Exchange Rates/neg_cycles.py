
def negative_cycle(n, edges):

    dist = {}
    prev = {}
    
    for i in range(n+1):
        if i == n:
            dist[i] = 0;
        else:
            dist[i] = float('inf');
        prev[i] = None;
    
    for j in range(n):
        edges.append(((n+1, j+1), 0));
    
    while n>0:
        for ((a,b),w) in edges:
            if dist[b-1] > dist[a-1] + w:
                    dist[b-1] = dist[a-1] + w;
                    prev[b-1] = a-1;           
        n-=1;
    
    for ((a, b), w) in edges:
        if dist[b-1] > dist[a-1] + w:
            return 1;
    
    return 0;


n = 4
edges = [((1,2), -5),((4,1), 2),((2,3), 2),((3, 1), 1)]

print(negative_cycle(n, edges))
