# Problem URL
https://practice.geeksforgeeks.org/problems/longest-distinct-characters-in-string5848/1

class Solution:

    def longestSubstrDistinctChars(self, S):
        
        substring = ""
        length = 0
        max_length = 0
        
        for i in S:
            if i not in substring:
                substring += i
                length += 1
                
            elif i in substring:
                if length > max_length:
                    max_length = length
                    
                substring = i
                length = 1
                
        return max_length
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends