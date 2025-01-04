class Solution(object):
    def thirdMax(self, nums):
        set_nums=set(nums)

        sor=sorted(set_nums,reverse=True)

        if len(sor) >= 3:
            return sor[2]
        else:
            return sor[0]
      
        