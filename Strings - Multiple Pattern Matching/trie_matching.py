class Node:
    def __init__ (self, value, symbol, parent):
        self.children = {}
        self.symbol = symbol;
        self.value = value
        self.parent = parent;
    
    def get_value(self):
        return self.value;
    
    def get_symbol(self):
        return self.symbol;
    
    def update_children(self, symbol, v):
        self.children[symbol]=v;
        
    def get_children(self):
        return self.children; 
    
    def get_parent(self):
        if self.parent!=None:
            return [self.parent.get_symbol(), self.parent.get_value()];
        else:
            return ['', -1];

def calculate_level_node(node):
    parent = node.get_parent();
    return parent[1]+1;       

def build_trie(patterns):
    # write your code here
    trie = [];
    levels = {};
    root_v = 0;
    root = Node(root_v, '', None);
    trie.append(root)
    levels[root_v] = [root];
    
    for string in patterns:
        curr_v = root_v;
        current = root;
        for i in range(len(string)):
            currSymbol = string[i];
            new_v = curr_v + 1;
            if new_v > len(trie)-1:
                new_n = Node(new_v, currSymbol, current);
                new_n_level = calculate_level_node(new_n);
                levels[new_n_level] = [new_n];
                
                trie.append(new_n);
                current.update_children(currSymbol, new_v)
                current = new_n; 
                curr_v = new_v;
            else:
                next_n = trie[new_v];
                next_n_level = calculate_level_node(next_n);
                level_nodes = levels[next_n_level]
                counter = 0;
                length_level_nodes = len(level_nodes);
                for i in range(length_level_nodes):
                    if currSymbol!=level_nodes[i].get_symbol():
                        counter+=1;
                    else:
                        current = level_nodes[i];
                        curr_v = level_nodes[i].get_value();
                if counter == length_level_nodes:
                   new_v = len(trie);
                   new_n = Node(new_v, currSymbol, current);
                   trie.append(new_n);
                   current.update_children(currSymbol, new_v);
                   levels[next_n_level].append(new_n);
                   
                   current = new_n;
                   curr_v = new_v;
         
    return trie 

def solve (text, patterns):
    result = [];
    l = len(text);
    counter = 0;
    trie = build_trie(patterns);
    
    while counter<l:
        symbol = text[counter]
        idx = counter
        curr_v = 0
        path = [];
        while True:
            curr_n = trie[curr_v];
            children = curr_n.get_children();
            no_of_children = len(children);
            
            if no_of_children==0:
                idx = path[0]
                result.append(idx)
                break
            elif symbol in children:
                curr_v = children.get(symbol)
                path.append(idx);
                idx+=1;
                if idx<l:
                    symbol=text[idx];
                else:
                    curr_n = trie[curr_v];
                    children = curr_n.get_children()
                    if len(children)==0:
                        idx = path[0];
                        result.append(idx);
                    break
            else:
                break     
        counter+=1;
    return result

text = 'AATCGGGTTCAATCGGGGT'
patterns = ['ATCG','GGGT']

#text = 'AAA'
#patterns = ['AA']
#text = 'A'
#patterns = ['A']

tree = build_trie(patterns);
#for node in tree:
 #   print((node.get_value()), node.get_symbol());
ans = solve(text, patterns)
print(ans)