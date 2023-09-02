#python code 

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        p = sorted(s)
        q = sorted(t)

        if p == q:
            return True
        else:
            return False

#-------------------------------------or----------------------------------#

#complete code : 
#cat - act


def isanagram(s,t):
    
    if len(s) != len(t):
        return False
    
    p = sorted(s) 
    q = sorted(t) 
        
    if p == q:
        return True
    
    else:
        return False


s = input()
t = input()
print(isanagram(s,t))
        
