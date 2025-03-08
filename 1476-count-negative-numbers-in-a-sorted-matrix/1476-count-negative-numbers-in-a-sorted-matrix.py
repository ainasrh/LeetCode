class Solution(object):
    def countNegatives(self, grid):
        result=0
        for arr in grid:
            count = len(list(filter(lambda x: x < 0,sorted(arr))))
            result+=count
        return result    
        
        
            