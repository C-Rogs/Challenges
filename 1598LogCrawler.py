class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        
        for op in logs:
            if op not in  ("./","../"):
                count += 1
            elif op == "../" and count > 0:
                count -= 1
        return count 