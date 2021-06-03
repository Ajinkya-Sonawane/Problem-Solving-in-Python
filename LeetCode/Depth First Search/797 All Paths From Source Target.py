# https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        stack = []
        target = len(graph)-1
        def dfs(node):
            stack.append(node)
            if node == target:
                res.append(stack.copy())
                return
            for neighbor in graph[node]:
                dfs(neighbor)
                stack.pop()
        
        for node in graph[0]:
            stack = [0]
            dfs(node)
        return res