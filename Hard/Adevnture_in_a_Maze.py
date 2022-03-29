# Problem URL
# https://practice.geeksforgeeks.org/problems/adventure-in-a-maze2051/1


class Solution:
    def FindWays(self, matrix):
        
        final = []
        
        def move(matrix, cellrow=0, cellcol=0, path = []):
                            
            lengthadj = len(matrix) - 1
            if cellrow == lengthadj and cellcol == lengthadj:
                if matrix[cellrow][cellcol] != 3:
                    path.append(matrix[cellrow][cellcol])
                final.append(path)
                
            if cellrow <= lengthadj and cellcol <= lengthadj:
                if (matrix[cellrow][cellcol] == 1 and cellcol == lengthadj) or (matrix[cellrow][cellcol] == 2 and cellrow == lengthadj):
                    return 0
    
                if matrix[cellrow][cellcol] == 1:
                    path.append(1)
                    cellcol += 1
                    move(matrix, cellrow, cellcol, path)
                    
                elif matrix[cellrow][cellcol] == 2:
                    path.append(2)
                    cellrow += 1
                    move(matrix, cellrow, cellcol, path)
                    
                elif matrix[cellrow][cellcol] == 3 and cellcol == lengthadj:
                    path.append(3)
                    cellrow += 1
                    move(matrix, cellrow, cellcol, path)
                    
                elif matrix[cellrow][cellcol] == 3 and cellrow == lengthadj:
                    path.append(3)
                    cellcol += 1
                    move(matrix, cellrow, cellcol, path)
                    
                elif matrix[cellrow][cellcol] == 3:
                    path.append(3)
                    move(matrix, cellrow + 1, cellcol, path.copy())
                    move(matrix, cellrow, cellcol + 1, path.copy())
        
        move(matrix)
        
        size = len(final)

        sums = [sum(i) for i in final]
        
        maxx = 0
        
        for i in sums:
            if i > maxx:
                maxx = i
    
        return [size, maxx]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            cur = list(map(int, input().split()))
            matrix.append(cur)
        obj = Solution()
        ans = obj.FindWays(matrix)
        for _ in ans:
            print(_, end = " ")
        print()

# } Driver Code Ends