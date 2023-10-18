import collections

# ByteDance is developing a new algorithm to implement in an upcoming software. The algorithm runs on a sequence of integers. Given an array data of size n, where the value of the ith integer is represented by the array data[i], the algorithm will run on data as:

# For every integer k, where 1 <= k < n. The algorithm will return the minimum common integer that occurs in all of the subarrays of the array data having length k.
# If there is no common integer occurring in any subarray of length k, then the algorithm will return -1.

# given an integer n, and an array data, find the array that the algorithm will return after running on data

# Example
# Given, n = 5, data = [4, 3, 3, 4, 2]

# subarrays | minimun comon integer
# [4][3][3][4][2] | -1
# [4,3][3,3][3,4][4,2] | -1
# [4,3,3],[3,3,4],[3,4,2] | 3
# [4,3,3,4][3,3,4,2] | 3
# [4,3,3,4,2] | 2

# Hence, the algorithm will return the array [-1, -1, 3, 3, 2] after running on data.

def func(n, arr):
    idx, n=collections.defaultdict(list),len(arr)

    for i,j in enumerate(arr):
        idx[j]+=[i]

    print(arr)
    print(idx)
        
    res=[float('inf')]*n
        
    # find the max gap between them.
    for num in idx:
        # This array contains -1 and n, and in between the idxes of each value
        x=[-1]+idx[num]+[n]
        print('x', x)
        # zip makes a tuple of items from ranges x[:-1], x[1:]
        print('zip')
        for i,j in zip(x[:-1],x[1:]):
            print(i, j, j-i)
        # For this number, find the max gap in consecutive indices, which includes -1 and n
        y=max(j-i for i,j in zip(x[:-1],x[1:]))
        # The max gap may occur between a num and either -1 or n.
        print('y', y)
        res[y-1]=min(res[y-1],num)

    print('res', res)
            
    for i in range(1,n):
        res[i]=min(res[i],res[i-1])

    for i in range(n):
        if res[i] == float('inf'): res[i] = -1

    print(res)
    
    return res




n = 5
data = [4, 3, 3, 4, 2]
sol = [-1, -1, 3, 3, 2]
assert(sol == func(n, data))