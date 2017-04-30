def reach(adj, x, y):
    n=len(adj);
    visited=[False for i in range(n)]
    
    def explore(v, visited, adj):
        visited[v]=True;
        neighbours=adj[v]
        no_n=len(neighbours);
        for j in range(no_n):
            w=neighbours[j];
            if not visited[w]:
                explore(w, visited, adj);
    if not visited[x]:
        explore(x, visited, adj);
    
    if visited[y]==True:
        return 1;
    else:
        return 0;

#adjacency_l=[[1,3],[0,2],[1,3],[2,0]];
#u=0
#v=3
#adjacency_l = [[1,3],[],[1],[2]]
#u = 0
#v = 3
adjacency_l = [[1],[],[1],[]]
u = 0
v= 3
print(reach(adjacency_l,u,v))