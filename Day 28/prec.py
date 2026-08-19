# Problem Statement: Ek string s di hogi. Aapko bina kisi repeating character ke sabse lambi substring ki length batani hai.

class Solution:
    def lengthOfLongestString(self , s:str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length , right - left + 1)

        return max_length
        
sol = Solution()
s = "stringstringssss"
print(sol.lengthOfLongestString(s))