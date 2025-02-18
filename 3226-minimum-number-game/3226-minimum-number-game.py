class Solution(object):
    def numberGame(self, nums):
        arr=[]
        alice=0
        bob=0
        nums.sort()
        for i in range(0,len(nums)-1,2):
            alice=nums[i]
            bob=nums[i+1]
            arr.append(bob)
            arr.append(alice)
        return arr    
