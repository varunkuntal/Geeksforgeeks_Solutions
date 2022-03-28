# Problem URL
# https://practice.geeksforgeeks.org/problems/generate-binary-string3642/1

class Solution:
    def generate_binary_string(self, s):
        
        final = []

        def removeNested(listy):
            for i in listy:
                if type(i) == list:
                    removeNested(i)
                else:
                    final.append(i)
    
        def gbs_nest(s):
		
            final = []
            
            if '?' not in s:
                return [s]
                
            else:
                list_s = list(s)
                list_s[list_s.index('?')] = '0'
    
                final.append(gbs_nest("".join(list_s)))
    
                list_s = list(s)
                list_s[list_s.index('?')] = '1'
    
                final.append(gbs_nest("".join(list_s)))
                        
            return final
            
        final_list = gbs_nest(s)
        
        removeNested(final_list)
        
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