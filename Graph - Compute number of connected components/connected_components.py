def number_of_components(adj):
    result = 0
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
                
    for j in range(n):
        if visited[j]==False:
            explore(j, visited, adj);
            result+=1;            
    
    return result

adjacency_l=[[1],[0,2],[1],[]]
print(number_of_components(adjacency_l))