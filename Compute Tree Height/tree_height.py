class TreeHeight:
        def read(self, n, parent):
                self.n = n;
                self.parent = parent;

                
        def compute_height(self):
            levels={};
            traversed_nodes=set();
            for node in range(self.n):
                new_level=1;
                locally_traversed=[];
                while node not in traversed_nodes:
                    if self.parent[node]!=-1:
                        new_level+=1;
                        traversed_nodes.add(node);
                        locally_traversed.append(node);
                        node=self.parent[node]
                    else:
                        traversed_nodes.add(node);
                        locally_traversed.append(node);
                        break
                if self.parent[node]!=-1:
                    current_level=levels.get(node);
                    for e in locally_traversed:
                        levels[e]=new_level+current_level-1;
                        new_level-=1;
                else:
                    for e in locally_traversed:
                        levels[e]=new_level;
                        new_level-=1;
            return max(levels.values());                         
 
#n1 = 10
#parent1 = [9,7,5,5,2,9,9,9,2,-1]
#n2 = 5;
#parent2 = [4,-1,4,1,1]  
n3 = 5
parent3 = [-1,0,4,0,3];                                                                                                                                    
tree = TreeHeight()
tree.read(n3, parent3)
print(tree.compute_height())