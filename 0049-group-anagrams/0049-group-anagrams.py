class Solution(object):
    def groupAnagrams(self, strs):
        hashing = {}

        if strs < 0 :
            return [""]
            
        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s in hashing:
                hashing[sorted_s].append(s)

            else:
                hashing[sorted_s] = [s]
            


        return hashing.values() 