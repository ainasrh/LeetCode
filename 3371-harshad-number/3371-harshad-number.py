class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        x_sum=sum(int(num) for num in str(x))

        if x%x_sum==0:
            return x_sum
        else:
            return-1
            