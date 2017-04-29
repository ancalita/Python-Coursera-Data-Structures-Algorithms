def inOrder(key, left, right):
    result = []
    stack=[];
    i=0;
    current=key[i];
    done=0;
    
    while (not done):
        if current is not None:
            stack.append([current,i]);
            i=left[i];
            if i!=-1:
                current=key[i];
            else:
                current=None
        else:
            if len(stack)>0:
                pair=stack.pop();
                result.append(pair[0]);
                i=pair[1];
                i=right[i]
                if i!=-1:
                    current=key[i];
                else:
                    current=None;
            else:
                done=1;
            
                
    return result

print(inOrder([4,2,5,1,3], [1,3,-1,-1,-1],[2,4,-1,-1,-1]))
print(inOrder([0,10,20,30,40,50,60,70,80,90],[7,-1,-1,8,3,-1,1,5,-1,-1],[2,-1,6,9,-1,-1,-1,4,-1,-1]))

def preOrder(key, left, right):
    result = []
    stack=[];
    i=0;
    done=0;
    
    while (not done):
        if i!=-1:
            current=key[i];
            stack.append([current,i]);
            result.append(current);
            i=left[i];
        else:
            if len(stack)>0:
                pair=stack.pop();
                curr_index=pair[1];
                i=right[curr_index];
            else:
                done=1;
            
    return result

print(preOrder([4,2,5,1,3], [1,3,-1,-1,-1],[2,4,-1,-1,-1]))
print(preOrder([0,10,20,30,40,50,60,70,80,90],[7,-1,-1,8,3,-1,1,5,-1,-1],[2,-1,6,9,-1,-1,-1,4,-1,-1]))

def postOrder(key, left, right):
    result = []
    stack=[]
    traversed_roots=set();
    i=0;
    root=key[i];
        
    while(True):
        while(root is not None):
            stack.append([root,i])
            traversed_roots.add(root)
            right_idx=right[i]
            if right_idx!=-1:
                right_child=key[right_idx];
                stack.append([right_child, right_idx]);
            left_idx=left[i]
            if left_idx!=-1:
                root=key[left_idx];
                i=left_idx;
            else:
                root=None;
        
        pair=stack.pop()
        root=pair[0]
        if root in traversed_roots:
            result.append(root);
            root=None;
        else:
            i=pair[1];
        
        if len(stack)==0:
            break
            
    return result 

print(postOrder([4,2,5,1,3], [1,3,-1,-1,-1],[2,4,-1,-1,-1]))
print(postOrder([0,10,20,30,40,50,60,70,80,90],[7,-1,-1,8,3,-1,1,5,-1,-1],[2,-1,6,9,-1,-1,-1,4,-1,-1]))