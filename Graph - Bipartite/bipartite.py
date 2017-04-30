import Queue

def bipartite(adj):
    
    frontier = Queue.Queue();
    explored = set();
    level = {};
    i=0;
    level[i] = 0;
    frontier.put(i);
    while not frontier.empty():
            neighbours = adj[i];
            explored.add(i);

            for e in neighbours:
                if e not in explored:
                    frontier.put(e);
                    level[e] = level[i]+1;

                if (level[i]%2==0 and level[e]%2==0) or (level[i]%2!=0 and level[e]%2!=0):
                        return 0;
                        
            i = frontier.get()
    return 1;

#adj=[[1,3,2],[0,2],[1,0],[0]]
adj= [[3],[4,3],[3],[1,2,0],[1]]
print(bipartite(adj))