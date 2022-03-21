#User function Template for python3
class Solution:
    def minRepeats(self, A, B):
        
        # If A is not in B for Length(B) > length(A), then B can never be substring of A repeated any number of times
        if (len(A) <= len(B)) and (A not in B):
            return -1
            
        # If A is larger string than B, we can find substring B in A in atmost A * 2 times 
        if (len(A) > len(B)): 
            if (B not in A * 2):
                return -1
            else:
                return 1 if B in A else 2
            
        # Ratio of lengths of B & A = max times to repeat A such that B could be substring of A
        # So there is finite amount of counts to look for substring
        length = int(len(B) / len(A))
        
        # Repeating by length + 2, post which B cannot be substring irrespective of the pattern
        for i in range(1, length+2):
            if B in A * i:
                return i
        
        return -1
            


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends