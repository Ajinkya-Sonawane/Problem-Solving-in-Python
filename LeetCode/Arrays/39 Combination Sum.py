# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target
        self.res = []
        self.total = len(candidates)
        self.candidates.sort()
        self.gen([],0)
        return self.res
        
    def gen(self,comb,start):        
        if comb and sum(comb) == self.target:
            self.res.append(comb)
            return
        if comb and sum(comb) > self.target:
            return
        for idx in range(start,self.total):
            self.gen(comb+[self.candidates[idx]],idx)
            
            