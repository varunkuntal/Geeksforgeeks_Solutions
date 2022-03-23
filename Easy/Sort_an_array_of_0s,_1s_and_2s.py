# Problem URL
# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

class Solution:
    def sort012(self,arr,n):
        dt = {}
        dt[0], dt[1], dt[2] = 0, 0,0
        for i in arr:
            if i == 0:
                dt[0] += 1
            if i == 1:
                dt[1] += 1
            if i == 2:
                dt[2] += 1
                
        arr.clear()
        # In a sorted array, order is zeroes, ones and twos
        arr = arr.extend([0] * dt[0] + [1] * dt[1] + [2] * dt[2])
        return arr
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends