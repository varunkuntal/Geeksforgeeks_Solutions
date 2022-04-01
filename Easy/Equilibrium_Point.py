# Problem URL
# https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1
# Logic for O(n) time complexity

class Solution:

    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        add = 0
        addreverse = 0
        
        
        # Taking two array of equal size to store cumulative sum from first to last & from last to first
        before = [0] * (N)
        after = [0] * (N)
        
        for i in range(N):
            add += A[i]
            addreverse += A[N - i - 1]
            before[i] = add
            after[N - i - 1] = addreverse
            
        # If at any index cumulative sums are equal, that is the equilibrium point
        for i in range(N):
            if before[i] == after[i]:
                return i+1
                
        return -1
            

#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends