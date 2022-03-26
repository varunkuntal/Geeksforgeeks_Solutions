# Problem URL
# https://practice.geeksforgeeks.org/problems/does-robot-moves-circular0414/1

class Solution:

    def isCircular(self, path):
        
        def walk(pathUnit, walkRecord, pointer):
            if pointer == 3 and pathUnit == 'L':
                pointer = 0
                
            elif pointer == 0 and pathUnit == 'R':
                pointer = 3
                
            elif pathUnit == 'L':
                pointer += 1
                
            elif pathUnit == 'R':
                pointer -= 1
                
            if pathUnit == 'G':
                
                if pointer == 0:
                    walkRecord[0] += 1
                if pointer == 1:
                    walkRecord[1] += 1
                if pointer == 2:
                    walkRecord[2] += 1
                if pointer == 3:
                    walkRecord[3] += 1
            
            return walkRecord, pointer
            
            
            
        walkRecord = [0] * 4
        
        pointer = 0
        
        for pathUnit in path:
            walkRecord, pointer = walk(pathUnit, walkRecord, pointer)
            
        if (walkRecord[0] + walkRecord[1]) == (walkRecord[2] + walkRecord[3]):
            return "Circular"
            
        else:
            return "Not Circular"
                
                
                
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        path = input()

        solObj = Solution()

        print(solObj.isCircular(path))
# } Driver Code Ends