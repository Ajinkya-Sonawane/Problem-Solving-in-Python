# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z'],
        }
        self.res = []
        self.dfs("",mappings,0,digits,len(digits))
        return self.res
        
    def dfs(self,s,mappings,index,digits,digit_len):
        if index == digit_len:
            if s:
                self.res.append(s)
            return
        
        letters = mappings[int(digits[index])]
        for char in letters:
            s += char
            self.dfs(s,mappings,index+1,digits,digit_len)
            s = s[:-1]
        
        