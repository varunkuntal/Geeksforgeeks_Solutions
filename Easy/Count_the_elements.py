# Problem URL
# https://practice.geeksforgeeks.org/problems/count-the-elements1529/1

def find(a,b,q):

    num_elem_list = [0] * len(q)
    
    for k, i in enumerate(q):
        a_elem = a[i]
        for j in b:
            if a_elem >= j:
                num_elem_list[k] += 1
                
    return num_elem_list

#{ 


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    qsz=int(input())
    q=[]
    for i in range(0,qsz):
        q.append(int(input()))
    ans=find(a,b,q)
    for i in range(0,qsz):
        print(ans[i])
    

