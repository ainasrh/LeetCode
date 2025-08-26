class Solution(object):
    def largestAltitude(self, gain):
        tsum = 0

        for i in range(len(gain)):
            gain[i] = tsum + gain[i]
            tsum = gain[i]
            
        gain.insert(0,0)
        
        return max(gain)
                