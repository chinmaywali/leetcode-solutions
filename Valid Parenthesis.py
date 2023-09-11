#Leetcode 20

'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
class Solution(object): '''


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)

            elif i == ')' or i == ']' or  i == '}':

                if not stack:
                    return False

                ob = stack.pop()

                if (i == ')' and ob!= '(') or (i == '}' and ob!= '{') or(i == ']' and ob!= '['):
                    return False

        return not stack


#-----------------------------or-------------------
#complete code 

def valid(s):
    stack = []
    
    
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
            
        elif i == ')' or i == ']' or  i == '}':
            if not stack:
                return False
            ob = stack.pop()
            if (i==')' and ob!='(') or (i==']' and ob!='[') or (i=='}' and ob!='{'):
                return False
                
    return not stack


s = input()
if valid(s):
    print("yes")
else:
    print("no")

