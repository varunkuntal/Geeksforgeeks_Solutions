# Problem URL:
# https://practice.geeksforgeeks.org/problems/count-of-strings-that-can-be-formed-using-a-b-and-c-under-given-constraints1135/1#

class Solution:
    def countStr(self, n):
        # Taking a mathematical approach of three cases. Using combinations nCr notation
        # Case 1: b = 1 time, c = 2 times, therefore a = n - 3 times. So nC1 * (n-1)C2 ways
        
        # Case 2: b = 0 time, c = 2 times, therefore a = n - 2 times. So nC2 ways
        
        # Case 3: b = 0 time, c = 1 time, therefore a = n - 1 times.  So nC1 ways
        
        # Case 4: b = 1 time, c = 1 time, therefore a = n - 2 times. So nC2 * 2! ways
        
        # Case 5: b = 1 time, c = 0 time,  therefore a = n - 1 time. So nC1 ways
        
        # case 6: b = 0 time, c = 0 time, therefore a = n time. So nCn = 1 way
        
        # Adding all the cases together and simplifying, we get n * (n - 1) * (n + 1) / 2 + (2 * n + 1)
        # We return the expression, hence no algorithm can beat the time to calculate
        
        return int(n * (n - 1) * (n + 1) / 2 + (2 * n + 1))
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends