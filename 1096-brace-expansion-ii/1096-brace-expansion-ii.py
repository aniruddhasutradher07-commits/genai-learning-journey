class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.index = 0
        self.n = len(expression)

        def parse_expr() -> set[str]:
            res = set()
            while self.index < self.n and expression[self.index] != '}':
                term = parse_term()
                res.update(term)
                
                if self.index < self.n and expression[self.index] == ',':
                    self.index += 1
            return res

        def parse_term() -> set[str]:
            res = {""}
            while (
                self.index < self.n 
                and expression[self.index] != '}' 
                and expression[self.index] != ','
            ):
                factor = parse_factor()
                res = {s1 + s2 for s1 in res for s2 in factor}
            return res

        def parse_factor() -> set[str]:
            if expression[self.index] == '{':
                self.index += 1  
                res = parse_expr()
                self.index += 1  
                return res
            else:
                char = expression[self.index]
                self.index += 1  
                return {char}

        final_set = parse_expr()
        return sorted(list(final_set))