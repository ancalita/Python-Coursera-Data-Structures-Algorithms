def acyclic(adj):
    n=len(adj)
    visited=[False for i in range(n)]
    recStack=[False for i in range(n)]
    
    def isCyclicHelper(v, visited,recStack, adj):
        
        if visited[v]==False:
            visited[v]=True;
            recStack[v]=True;
            neighbours=adj[v];
            no_n=len(neighbours);
            for j in range(no_n):
                w=neighbours[j];
                if not visited[w] and isCyclicHelper(w,visited, recStack, adj):
                    return True;
                elif recStack[w]:
                    return True;
        recStack[v]=False;
        return False;
            
    for i in range(n):
       if isCyclicHelper(i, visited, recStack, adj):
           return 1;
    
    return 0;
        
adj=[[1],[2],[0],[0]]
print(acyclic(adj))

adj2=[[1,2,3],[2,4],[3,4],[],[]]
print(acyclic(adj2))