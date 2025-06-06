from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        result = []
        counter_map = Counter([str(i) for i in nums])
        for i in counter_map.most_common(k):
            result.append(int(i[0]))
        return result
