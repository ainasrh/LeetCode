class Solution(object):
    def sumZero(self, n):
        # Use list directly instead of set to preserve order (optional)
        result = []

        for i in range(1, n // 2 + 1):
            result.extend([i, -i])

        if n % 2 == 1:
            result.append(0)

        return result
