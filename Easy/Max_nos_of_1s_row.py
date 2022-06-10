# Problem URL: https://practice.geeksforgeeks.org/problems/maximum-no-of-1s-row3027
class Solution:
    def maxOnes (self, Mat, N, M):
       
        r = 0
        c = M-1
       
        rowindex = -1
       
        while r != N and c != -1:

            if Mat[r][c] == 1:
                rowindex = r
                c -= 1
               
            else:
                r += 1
               
        return rowindex

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        size = input().strip().split()
        r = int(size[0])
c = int(size[1])
line = list(map(int,input().split()))
matrix = [ [0 for _ in range(c)] for _ in range(r) ]
        for i in range(r):
for j in range(c):
matrix[i][j] = line[i*c+j]
        ob = Solution()
        print(ob.maxOnes(matrix,r,c))