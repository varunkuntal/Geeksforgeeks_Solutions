# Problem URL
# https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1

class Solution:    
    #Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        loop = (N // K) + 1
        start = 0
        end = K
        for i in range(loop):
            arr[start:end] = arr[start:end][::-1]
            start = end
            end = (end + K) if i != N // K else len(arr)
        return arr
            

#{ 
#  Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends