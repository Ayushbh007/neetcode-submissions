class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        flag=True
        maine = strs[0]
        for i in range(1,len(maine)+1):
            check=maine[:i]
            for j in range(1,len(strs)):
                if check not in strs[j]:
                    flag=False
            
            if flag==True:
                ans=check

        return ans