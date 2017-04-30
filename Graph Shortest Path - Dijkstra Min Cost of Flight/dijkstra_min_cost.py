
import heapq
        
def distance(adj, cost, s, t):

    dist = {}
    prev = {}
    h = [];
    
    for i in range(len(adj)):
        if i == s:
            dist[i] = 0;
        else:
            dist[i] = float('inf');
        heapq.heappush(h,(dist[i], i));
        prev[i] = None;
    
    while len(h)>0:
            (d, u) = heapq.heappop(h);
            neighbours = adj[u];
            for k in range(len(neighbours)):
                e = neighbours[k];
                if dist[e] > dist[u] + cost[u][k]:
                    dist[e] = dist[u] + cost[u][k];
                    prev[e] = u;
                    new_list=[];
                    for (d, v) in h:
                        if v == e:
                            new_list.append((dist[e], v))
                        else:
                            new_list.append((d, v))
                    h = new_list;
                    heapq.heapify(h);
    copy_t = t
                             
    while None != prev[t]:
            x = prev.get(t)
            if x == s:
                return dist[copy_t];
                break;
            else:
                t = x;
    return -1;


#adj = [[1,2],[2],[],[0]]
#cost = [[1,5],[2],[],[2]]
#s=0
#t=2

#adj= [[1,2],[2,3,4],[1,4,3],[],[3]]
#cost= [[4,2],[2,2,3],[1,4,4],[],[1]]
#s=0
#t=4

#adj = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[]]
#cost = [[1],[1],[1],[1],[1],[1],[1],[1],[1],[]]
#s=0
#t=9

#adj = [[]]
#cost = [[0]]
#s=0
#t=0

#adj = [[1,2],[2],[],[]]
#cost = [[1,5], [2], [], []]
#s=1
#t=3

adj = [[1,2], [2], []]
cost =  [[7,5], [2], []]
s=2
t=1

print(distance(adj,cost,s,t))