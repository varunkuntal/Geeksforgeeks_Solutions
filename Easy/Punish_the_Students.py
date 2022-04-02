# Problem URL
# https://practice.geeksforgeeks.org/problems/punish-the-students5726/1

class Solution:
    def shouldPunish (self, roll, marks, n, avg):
        
        markssum = sum(marks)
        
        for i in range(n):
            for j in range(n-1-i):
                if roll[j] > roll[j+1]:
                    
                    roll[j], roll[j+1] = roll[j+1], roll[j]
                    markssum -= 1
                    
        if int(markssum / n) <= avg:
            return 0
        return 1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n, avg = input ().split ()
    n = int (n)
    avg = float (avg)
    roll = list(map(int, input().split()))
    marks = list(map(int, input().split()))
    ob=Solution()
    print (ob.shouldPunish (roll, marks, n, avg))
# } Driver Code Ends