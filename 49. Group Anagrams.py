from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        result = []
        for i in strs:
            item = ''.join(sorted(i))
            hashmap[item].append(i)

        for i in hashmap.values():
            result.append(i)
        return result
