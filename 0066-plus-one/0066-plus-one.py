class Solution(object):
    def plusOne(self, digits):
        num=int("".join(map(str,digits)))


        num_str=str(num+1)
        result=[int(digit) for digit in num_str ]

        return result


