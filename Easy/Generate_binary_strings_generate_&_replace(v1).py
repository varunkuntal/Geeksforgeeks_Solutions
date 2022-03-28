# Problem URL
# https://practice.geeksforgeeks.org/problems/generate-binary-string3642/1


class Solution:
    def generate_binary_string(self, s):
        if "?" not in s:
            return [s]
        
        S = s.split("?")
        total_qms = s.count("?")
        total_combs = 2 ** total_qms
        combined = []
        final = []

        for j in range(total_qms):
            binarycolumn = ""
            
            for i in range(total_combs):
            
                
                if i % (2 ** (j + 1)) < (2 ** (j + 1)) / 2:
                    binarycolumn += "0"
                else:
                    binarycolumn += "1"
                    
            combined.append(binarycolumn)
            
        combined.reverse()
        
        combined = list(zip(*combined))
        
        
        indexes = [i for i, j in enumerate(s) if j == "?"]
        
        for i in combined:
            dup = list(map(str, s))
            for j, k in enumerate(i):
                dup[indexes[j]] = k
            final_str = "".join(dup)
            final_str = "".join(final_str.split())
            final.append(final_str)
            
        return final
		
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        s= input()
        ob = Solution()
        ans = ob.generate_binary_string(s)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends