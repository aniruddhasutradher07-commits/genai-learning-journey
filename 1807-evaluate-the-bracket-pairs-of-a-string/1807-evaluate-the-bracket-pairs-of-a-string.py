class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_map = {k: v for k, v in knowledge}
        
        result = []
        current_key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                key_str = "".join(current_key)
                result.append(knowledge_map.get(key_str, "?"))
                current_key.clear()
                in_bracket = False
            else:
                if in_bracket:
                    current_key.append(char)
                else:
                    result.append(char)
                    
        return "".join(result)