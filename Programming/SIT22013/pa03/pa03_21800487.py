#pa03 윤사무엘

# get data
get_data=lambda : [int(x) for x in input().split()]
n1=int(input())
f1=[0]*n1
for i in range(n1):
    f1[i]=get_data()
n2=int(input())
f2=[0]*n2
for i in range(n2):
    f2[i]=get_data()
pq=get_data()
p,q=pq[0],pq[1] # 구해야하는 범위의 시작(=p), 끝(=q)


# function 
def mergeSort(list1,list2): # 두함수를 합치면서 정렬하는 함수
    l1=len(list1)
    l2=len(list2)
    result=[]
    threshold=0
    idx1=0
    idx2=0
    while idx1!=l1 or idx2!=l2:
        if idx1==l1:
            if list2[idx2][1]>threshold:
                result=result+list2[idx2:]
                return result
            else:
                idx2+=1
        elif idx2==l2:
            if list1[idx1][1]>threshold:
                result=result+list1[idx1:]
                return result
            else:
                idx1+=1
        elif list1[idx1][0]>list2[idx2][0]:
            if list2[idx2][1]>threshold:
                result.append(list2[idx2])
                threshold=list2[idx2][1]
                idx2+=1
            else:
                idx2+=1
        elif list1[idx1][0]<list2[idx2][0]:
            if list1[idx1][1]>threshold:
                result.append(list1[idx1])
                threshold=list1[idx1][1]
                idx1+=1
            else:
                idx1+=1
        elif list1[idx1][0]==list2[idx2][0]:
            if list1[idx1][1]>=list2[idx2][1]:
                result.append(list1[idx1])
                threshold=list1[idx1][1]
                idx1+=1
                idx2+=1
            else:
                result.append(list2[idx2])
                threshold=list2[idx2][1]
                idx1+=1
                idx2+=1
    return result

def binarySearch(lst,key):  # 이진탐색 
    low=0
    high=len(lst)-1
    while high>=low:
        mid=(low+high)//2
        if key<lst[mid][0]:
            high=mid-1
        elif key==lst[mid][0]:
            return mid     # 1. key값이 존재하는경우 key값의 index return
        else:
            low=mid+1
    return high            # 2. key값이 존재하지않는경우 키값 이전 index return


# main
step_func=mergeSort(f1,f2)  # list merge
start=binarySearch(step_func,p) # p,q값의 인덱스 탐색
if start<0:
    start=0
end=binarySearch(step_func,q)

result=0    # 결과값

if start==len(step_func)-1:         
    result=(q-p+1)*step_func[-1][1]
else:    
    for i in range(start,end+1):
        if i==start:
            if p<step_func[i][0]:
                result+=step_func[i][1]*(step_func[i+1][0]-step_func[i][0])
            else:
                result+=step_func[i][1]*(step_func[i+1][0]-p)
        elif i==end:
            if step_func[end][0]==q:
                result+=step_func[end][1]
            else:
                result+=step_func[end][1]*(q-step_func[end][0]+1)
        else:
            result+=step_func[i][1]*(step_func[i+1][0]-step_func[i][0])

# Output
print(result%10007)

        
            
    
