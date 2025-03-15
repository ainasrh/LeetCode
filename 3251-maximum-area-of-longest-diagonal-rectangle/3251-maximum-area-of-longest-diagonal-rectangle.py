class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        if not dimensions:
            return 0
        max_d,max_a=0,0
        for w,h in dimensions:
            sqr_sum= w**2 + h**2
            if sqr_sum > max_d:
                max_d=sqr_sum
                max_a=w*h
            elif sqr_sum == max_d and w*h >max_a:
                max_a=w*h
        return  max_a    