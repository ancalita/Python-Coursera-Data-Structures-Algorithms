def optimal_points(segments):
    
    points=[];
    sorted_segments=sorted(segments, key=lambda s:s[1]);
    
    while len(sorted_segments)>0:
        copy = sorted_segments[:]
        point = sorted_segments[0][1]
        
        for s in copy:
            if s[0]<=point<=s[1]:
                sorted_segments.remove(s);
        points.append(point);
          
    return points; 


#list_of_points=optimal_points([(1,3),(2,5),(3,6)]);
list_of_points = optimal_points([(4,7), (1,3), (2,5), (5,6)])
print(len(list_of_points));
for p in list_of_points:
    print(p, end = ' ');