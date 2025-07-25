"""
Alice is allowed the following operations:
1. Fully fill a bucket.
2. Empty a bucket.
3. Pour bucket into another, up until the other bucket's capacity.

Note that Alice doesn't know how to measure water in any other way, e.g. she can't pour 1/2 of a bucket into another because her measurement would be inaccurate.

Example: buckets have capacity 3 and 5. Alice is asked to measure 4.
Let's denote buckets' contents by a tuple (a, b) where 0 <= a <= 3 and 0 <= b <= 5.
We start with (0, 0) and can follow these steps:
1. Fill up the big bucket (0, 5)
2. Pour to the smaller one (3, 2)
3. Empty the small one (0, 2)
4. Pour water from big to small (2, 0)
5. Fill up the big one (2, 5)
6. Pour water from big to small (3, 4)

Your task is to help Alice determine the shortest sequence of steps that gets desired capacity.

Here she took 6 steps to get to 4 gallons of water.
"""


from collections import deque
from copy import copy


class solution():
    def __init__(self, buckets: list[int], target:int) -> int:

        self.target = target
        self.buckets = buckets # max capacity
        self.n = len(buckets)
        self.visited = [] # key: list of volumes

        assert self.n == 2


    def done(self, current_bucket):
        for x in current_bucket:
            if x == self.target:
                return True
        return False

    def explore(self):
        current_bucket = [0] * self.n
        self.visited.append(current_bucket)
        done = self.done(current_bucket)
        step = 0
        queue = deque([ (current_bucket, step) ])
        
        while len(queue) > 0:

            base_bucket, step = queue.popleft()
            for bucket_id in range(self.n):
                current_bucket = self.fill(copy(base_bucket), bucket_id)
                # print(current_bucket)
                if current_bucket not in self.visited:
                    if self.done(current_bucket):
                        return step+1
                    self.visited.append( current_bucket )
                    queue.append( (current_bucket, step+1) )

            for bucket_id in range(self.n):
                current_bucket = self.empty(copy(base_bucket), bucket_id)
                if current_bucket not in self.visited:
                    if self.done(current_bucket):
                        return step+1
                    self.visited.append( current_bucket )
                    queue.append( (current_bucket, step+1) )

            for a, b in [(0,1), (1,0)]:
                current_bucket = self.pour(copy(base_bucket), a, b)
                if current_bucket not in self.visited:
                    if self.done(current_bucket):
                        return step+1
                    self.visited.append( current_bucket )
                    queue.append( (current_bucket, step+1) )
            # print(queue)
            print(self.visited)





    #1. Fully fill a bucket.
    def fill(self, current_bucket:list[int], bucket_id:int):
        current_bucket[bucket_id] = self.buckets[bucket_id]
        return current_bucket

    #2. Empty a bucket.
    def empty(self, current_bucket:list[int], bucket_id:int):
        current_bucket[bucket_id] = 0
        return current_bucket

    # 3. Pour bucket into another, up until the other bucket's capacity.
    def pour(self, current_bucket:list[int], initial:int, receiver:int):
        receiving_capacity = self.buckets[receiver] - current_bucket[receiver]
        poured = min(receiving_capacity, current_bucket[initial])
        current_bucket[receiver] += poured
        current_bucket[initial] -= poured
        return current_bucket

# 3325, 1233355, 555
#121, 330, 11
sol = solution(buckets=[121,330], target=11)

step = sol.explore()
print(step)










