import heapq

def write_response(num_workers,m, h, jobs):
        if m<=num_workers:
            for i in range(m):
                job_in_progress=heapq.heappop(h);
                print(job_in_progress[1],job_in_progress[0]);
        else:
            for i in range(num_workers,0,-1):
                duration=jobs[-i];
                finish_time=duration+h[0][0];
                job_in_progress=heapq.heappushpop(h, (finish_time, h[0][1]));
                print(job_in_progress[1], job_in_progress[0]) 

def assign_jobs(num_workers,m,h,jobs):
        for i in range(num_workers):
            heapq.heappush(h,(0,i));
        
        for j in range(num_workers,m,+1):
            
            duration=int(jobs[j-num_workers]);
            finish_time=int(duration+h[0][0]);
            x=heapq.heappushpop(h,(finish_time,h[0][1]));
            print(x[1],x[0])
            
        return h;

#h=assign_jobs(4,20,[], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]);
#write_response(4,20,h,[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

h= assign_jobs(2,5,[], [1,2,3,4,5]);
write_response(2,5,h,[1,2,3,4,5])