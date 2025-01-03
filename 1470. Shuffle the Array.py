class Solution:
    def shuffle(self, nums, n):
        num_1 = nums[:n]
        num_2 = nums[n:]
        shuffle_arr = []
        for i in range(len(num_1)):
            shuffle_arr.append(num_1[i])
            shuffle_arr.append(num_2[i])
        return shuffle_arr
