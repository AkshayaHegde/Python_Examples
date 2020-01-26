class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        
        maxcount=1;
        for i in range(0,len(s)-1):
            point=i
            localMaxcount=1
            charList=[]
            charList.append(s[i])
            for j in range(i+1,len(s)):
                if s[point]!=s[j] and s[j] not in charList:
                    localMaxcount=localMaxcount+1
                    point=j
                    charList.append(s[j])
                else:
                    break
            
            if maxcount<localMaxcount:
                maxcount= localMaxcount
        return maxcount