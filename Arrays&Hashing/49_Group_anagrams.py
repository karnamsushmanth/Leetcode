# 49. Group Anagrams 

# Description
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:   
            # hat == sorted(s) == ["a","h","t"]  
            # join means aht 
            # append means aht:[hat]
            sortedS=''.join(sorted(s))
            result[sortedS].append(s)
        return list(result.values())
    
    # time complexity : O(m*n logn)
    # space complexity :O(m*n)
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:   
            # hat == sorted(s) == ["a","h","t"]  
            # join means aht 
            # append means aht:[hat]
            count=[0]* 26
            # [0,0,0,0,0,.......26]
            for c in s:
                count[ord(c)-ord('a')]+=1
                # will update for cat [1,0,1,0,0,0,0,0,0,1.....26]
            result[tuple(count)].append(s)
            # act : [cat]
        return list(result.values())
      
    
            