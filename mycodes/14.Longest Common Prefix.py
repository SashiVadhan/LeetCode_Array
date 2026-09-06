class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
            if prefix == "":
                return ""
        return prefix

# Time Complexity = O(n × m)
# 0ms
# 19.4mb
