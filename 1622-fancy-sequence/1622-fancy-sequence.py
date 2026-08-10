class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.seq = []
        self.mult = 1
        self.add = 0
        
    def append(self, val: int) -> None:
        inv_mult = pow(self.mult, self.MOD - 2, self.MOD)
        raw = (val - self.add) * inv_mult % self.MOD
        self.seq.append(raw)
        

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD
        

    def multAll(self, m: int) -> None:
        self.mult = self.mult * m % self.MOD
        self.add = self.add * m % self.MOD

        

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % self.MOD    
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)