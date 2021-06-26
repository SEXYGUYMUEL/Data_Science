#21800487 윤사무엘 pa02

# input data
get_data=lambda : [int(x) for x in input().split()]
data0=get_data()
n,k=data0[0],data0[1]
data1=[0]*n
for i in range(n):
    data1[i]=get_data() # ex) [[4,3],[10,15],[2,2],[5,1]]

# data sort
data1.sort(key=lambda x:x[1])

# new list
people=[0]*n # building capacity
idx=[0]*n    # building coordinates
for i in range(n):
    people[i]=data1[i][0]
    idx[i]=data1[i][1]

# make dynamic programming list -> memorization
dp=[0]*(data1[-1][1]+1)     # len(dp) == last building coordinate
for i in range(n):          # mapping building 
    dp[idx[i]]=people[i]
s=0
for i in range(len(dp)):    # accumulate sum
    s+=dp[i]
    dp[i]=s

# make cache list 
# cache[index] = Maximum capacity with the i-th building to the right end of the hospital's range
cache=[0]*(n)
cache[0]=dp[0]
pivot=0 # start point
flag=0  # range check

for i in range(n):
    if i==0: t=idx[i]
    else:
        t=(idx[i]-idx[i-1]) # t = distance between building
    if t>(2*k):         # (2*k) = hospital acceptable range
        pivot=idx[i]
        flag=0
        cache[i]=people[i]  # if t>(2*k) ->  new pivot & flag initialization
    else:
        flag=flag+t    
        if flag<=(2*k):
            if pivot==0: # when starting with coordinate 0    
                cache[i]=dp[idx[i]]
            else:
                cache[i]=dp[idx[i]]-dp[pivot-1] # sum(A[k:k+p])= S[k+p]-S[k-1]
        elif flag>(2*k):
            ts=idx[i]-(2*k)# calculate pivot gap 
            pivot=ts       # pivot update
            cache[i]=dp[idx[i]]-dp[pivot-1]
            flag=(2*k) # flag reset
# Output
print(max(cache))


