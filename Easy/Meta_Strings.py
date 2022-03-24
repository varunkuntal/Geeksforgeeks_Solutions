# Problem URL
# https://practice.geeksforgeeks.org/problems/meta-strings5713/1

class Solution:
    def metaStrings(self, S1, S2):
        
        lens1 = len(S1)
        lens2 = len(S2)
        
        # Exit if base conditions are not met
        if lens1 != lens2 or S1 == S2 or lens1 < 2 or lens2 < 2:
            return 0
            
        # List containing element wise comparison of the two strings
        boolComparison = [i == j for i, j in zip(S1, S2)]
        
        # Get indexes where elements from the two strings were not equal
        falsePositions = [i for i, j  in enumerate(boolComparison) if j == False]
        
        # If more or less than exactly two elements in the two string are not equal, it is not "Meta String"
        if len(falsePositions) != 2:
            return 0
            
        # If the two positions from the two string have their elements interchanged,
        # then and only then it is a Meta String.
        if S1[falsePositions[1]] == S2[falsePositions[0]] and S1[falsePositions[0]] == S2[falsePositions[1]]:
            return 1
        else:
            return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        obj = Solution()
        if obj.metaStrings(S1, S2):
            print(1)
        else:
            print(0)
# } Driver Code Ends