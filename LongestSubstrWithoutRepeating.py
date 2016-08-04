class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # str is substr[start, end] len is end - start + 1
        start = 0
        visited_chars = set()
        res = ""
        for end in xrange(len(s)):
            currChar = s[end]
            if currChar not in visited_chars:
                visited_chars.add(currChar)
                curr_len = end - start + 1
                if curr_len > len(res):
                    res = s.substr(start, end + 1)
            else:
                while s[start] != currChar:
                    visited_chars.remove(s[start])
                    start += 1
                start += 1
        return res

s = Solution()
s.lengthOfLongestSubstring("abccd")

