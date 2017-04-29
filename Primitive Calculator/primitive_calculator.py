def optimal_sequence(n):
     sequence=[];
     dictionary={};
     for i in range(n):
         if i==0:
             dictionary[0]=0;
         else:
             if i%3==0 and i%2==0:
                 m=min(dictionary.get(i//3),dictionary.get(i//2), dictionary.get(i-1));
                 dictionary[i]=m+1;
             if i%3==0 and i%2!=0:
                 m=dictionary.get(i//3);
                 dictionary[i]=m+1;
             elif i%2==0 and i%3!=0:
                m=dictionary.get(i//2);
                dictionary[i]=m+1;
             else:
                dictionary[i]=dictionary.get(i-1)+1;
     while n>=1:
        sequence.insert(0,n);
        if n%3==0 and n%2==0:
            m=min(dictionary.get(n//3), dictionary.get(n//2), dictionary.get(n-1));
            if dictionary.get(n//3)==m:
                n=n//3;
            elif dictionary.get(n//2)==m:
                n=n//2;
            else:
                n=n-1;
        elif n%3==0 and n%2!=0:
            if dictionary.get(n//3)>dictionary.get(n-1):
                n=n-1;
            else:
                n=n//3;
        elif n%2==0 and n%3!=0:
            if dictionary.get(n//2)>dictionary.get(n-1):
                n=n-1;
            else:
                n=n//2;
        else:
            n=n-1;         
     return sequence;

print optimal_sequence(96234);