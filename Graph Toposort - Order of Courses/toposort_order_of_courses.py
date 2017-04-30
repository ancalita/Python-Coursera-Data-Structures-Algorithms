
def dfs(adj, parents, added, order, x ):
    
        neighbours=adj[x];
        len_neighbours=len(neighbours);
        if len_neighbours==0:
                order.insert(0,x);
                added[x]=True;
                for j in parents[x]:
                    adj[j].remove(x);
        else:
            for item in neighbours:
                if not added[item]:
                    dfs(adj, parents, added, order, item);

def toposort(adj):
    
    n=len(adj)
    final_order=[]
    added = [False for i in range(n)]
    parents=[[] for i in range(n)]
    
    for i in range(n):
        parent=i;
        children=adj[i]
        for child in children:
            parents[child].append(parent);
    
    while added.count(True)<n:
        for i in range(n):
            if not added[i]:
                dfs(adj, parents, added, final_order, i);
                
    return final_order;
    
adjacency_l_1=[[],[0,2,4,3],[0,3,4],[0,4],[0]]
edges=[(4,5),(3,1),(2,1),(2,3),(5,1),(2,5),(4,1),(2,4),(3,4),(3,5)]
order_1= toposort(adjacency_l_1)
print(order_1)

adjacency_l_2 = [[1],[],[0],[0]]
order_2 = toposort(adjacency_l_2)
print(order_2)

adjacency_l_3 = [[],[],[0],[]]
order_3 = toposort(adjacency_l_3)
print(order_3)

adjacency_l_4 = [[],[0],[1,0],[2,0],[1,2]]
order_4 = toposort(adjacency_l_4);
print(order_4)