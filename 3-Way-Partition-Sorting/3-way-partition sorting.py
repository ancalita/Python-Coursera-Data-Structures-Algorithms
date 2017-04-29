import random

def partition3(a, l, r):
    #write your code here
    x=a[l];
    m1=l;
    m2=r;
    i=l;
    while i<=m2:
        if a[i]<x:
            a[m1], a[i]=a[i], a[m1];
            m1+=1;
            i+=1;
        elif a[i]>x:
            a[m2],a[i]=a[i],a[m2];
            m2-=1;
        else:
            i+=1;
    #a[l+m1],a[m1]=a[m1], a[l+m1];
    #a[m1],a[m2]=a[m2], a[r-m2];
    
    return m1,m2;


def randomized_quick_sort(a, l, r):
    if l>=r:
        return a;
    else:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m1,m2 = partition3(a, l, r)
        randomized_quick_sort(a, l, m1 - 1);
        randomized_quick_sort(a, m2+1, r);

sequence = [2,3,9,2,2]
n = len(sequence)
randomized_quick_sort(sequence, 0, n - 1)
for i in sequence:
    print(i, end=' ')