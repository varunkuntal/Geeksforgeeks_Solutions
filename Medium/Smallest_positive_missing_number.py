#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    # def missingNumber(self,arr,n):
        
    #     positives = list(set([i for i in sorted(arr) if i > 0]))
        
        
    #     N = [i for i in range(1, len(positives) + (1 if 0 in positives else 2))]
        
        
    #     for i, j in enumerate(positives):
    #         if N[i] != j:
    #             return N[i]
                
    #     try:
    #         return N[i] + 1
    #     except:
    #         return 1
    
    def missingNumber(self,arr,n):
        A=[0]*1000000
        for i in range(n):
           if arr[i] > 0:
               A[arr[i]]=1
        for i in range(1,len(A)):
           if A[i]==0:
               return i

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends