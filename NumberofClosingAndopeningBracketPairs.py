class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count_num=0
        for i in range(0,len(s)-1):
            
            if s[i]=="(":
                for j in range(i+1,len(s)):
                    
                    if s[j]==")":
                        count_num=count_num+1
        return count_num