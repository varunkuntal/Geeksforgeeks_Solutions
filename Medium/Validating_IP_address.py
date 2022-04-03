# Problem URL
# https://practice.geeksforgeeks.org/problems/validate-an-ip-address-1587115621/1

def isValid(s):
    
    def leadzerocheck(s):
        if len(s) > 1:
            if s[0] == '0' and s[1] != '0':
                return True
        if len(s) == 3:
            if s[1] == '0' and s[2] != '0':
                return True
    
    S = s.split(".")
    
    if not len(S) == 4:
        return 0
        
    for k, i in enumerate(S):
        if len(i) > 3 or len(i) < 1:
            return 0
            
        if leadzerocheck(i):
            return 0
            
        if not i.isdigit():
            return 0

        intpart = int(float(i))
        
        if intpart < 0 or intpart > 255:
            return 0
            
        if k == 0 and len(i) > 1:
            if (all(j == '0' for j in i)):
                return 0
                
    return 1
    
    
def leadzerocheck(s):
    if len(s) > 1:
        if s[0] == 0 and s[1] != 0:
            return True
    if len(s) == 3:
        if s[1] == 0 and s[2] != 0:
            return True


#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends