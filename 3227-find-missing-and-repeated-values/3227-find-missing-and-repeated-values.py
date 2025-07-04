class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        result = []
        flat = [num for row in grid for num in row]
        print(flat)
        count= Counter(flat)
        repeated = [num for num,freq in count.items() if freq > 1]
        result.append(int("".join(map(str,repeated))))
        flat_set = set(flat)
        missing = ([i for i in range(1,len(flat)+1) if not i in flat_set])
        result.append(int("".join(map(str,missing))))
        return result
                