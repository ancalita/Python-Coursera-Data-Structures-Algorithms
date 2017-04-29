class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.hash_table=[[] for i in range(self.bucket_count)];
        
    def _hash_func(self, s):
        ans = 0
        for i in range(len(s)-1,-1,-1):
            ans += (int(ord(s[i]))* (self._multiplier**i));
        ans=(ans%self._prime + self._prime)%self._prime;
        return ans % self.bucket_count

    def write_chain(self, chain):
        print(' '.join(map(str, chain)));

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.hash_table[query.ind])
        else:
             hash_bucket=self._hash_func(query.s) 
             if query.type == 'find':
                if query.s in set(self.hash_table[hash_bucket]):
                    print('yes')
                else:
                    print('no')
             elif query.type == 'add':
                if query.s not in set(self.hash_table[hash_bucket]):
                    self.hash_table[hash_bucket].insert(0,query.s);
                    
             else:
                if query.s in set(self.hash_table[hash_bucket]):
                    self.hash_table[hash_bucket].remove(query.s);
                    
    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

bucket_count = 5
proc = QueryProcessor(bucket_count)
proc.process_queries()