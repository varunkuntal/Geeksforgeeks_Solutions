#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        if len(A) != len(B):
            return 0
        
        
        da = {}
        db = {}

        for i in range(len(A)):
            if da.get(A[i]):
                da[A[i]] += 1
            else:
                da[A[i]] = 1
                
            if db.get(B[i]):
                db[B[i]] += 1
            else:
                db[B[i]] = 1
        

        if da == db:
            return 1
                    
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends