class Solution:
    def calPoints(self, operations):
        solution = []
        for i in operations:
            if i == '+':
                solution.append(solution[-1] + solution[-2])
            elif i == 'C':
                solution.pop()
            elif i == 'D':
                solution.append(solution[-1] * 2)
            else:
                solution.append(int(i))
        return sum(solution)
