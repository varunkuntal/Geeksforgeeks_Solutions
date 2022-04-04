#User function template for Python

class Solution:    
    
    def __init__(self, idx=0):
        self.idx = idx

    def binarysearch(self, arr, n, k):
        
        if not arr:
            return -1

        mid = len(arr) // 2

        if arr[mid] == k:
            self.idx += mid
            return self.idx

        if arr[mid] > k:
            left = arr[:mid]
            return self.binarysearch(left, len(left), k)

        else:
            right = arr[mid+1:]
            self.idx += mid+1
            return self.binarysearch(right, len(right), k)

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends