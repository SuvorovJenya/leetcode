from collections import defaultdict
class Solution:
    def isAnagram(self, s, t):
        anagram_dict = defaultdict(int)

        for i in s:
            anagram_dict[i] += 1

        for i in t:
            anagram_dict[i] -= 1

        for i in anagram_dict.values():
            if i != 0 :
                return False
        return True 
