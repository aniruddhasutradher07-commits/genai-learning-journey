from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        R = len(classroom)
        C = len(classroom[0])
        
        litter_idx = {}
        start = None
        
        # Parse the grid to locate the starting point and index all litter
        for r in range(R):
            for c in range(C):
                val = classroom[r][c]
                if val == 'S':
                    start = (r, c)
                elif val == 'L':
                    litter_idx[(r, c)] = len(litter_idx)
                    
        k = len(litter_idx)
        # If there is no litter to collect, zero moves are required
        if k == 0:
            return 0
            
        target_mask = (1 << k) - 1
        
        # visited[r][c][mask] will track the *maximum* energy recorded at that specific state
        visited = [[[-1] * (1 << k) for _ in range(C)] for _ in range(R)]
        
        # Queue stores: (row, col, collected_mask, current_energy)
        q = deque([(start[0], start[1], 0, energy)])
        visited[start[0]][start[1]][0] = energy
        
        moves = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            size = len(q)
            for _ in range(size):
                r, c, mask, e = q.popleft()
                
                # If energy reaches 0 and we are not on a Reset area, we cannot make any further moves from here
                if e == 0:
                    continue
                    
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < R and 0 <= nc < C and classroom[nr][nc] != 'X':
                        cell = classroom[nr][nc]
                        
                        # Process energy transitions
                        next_e = energy if cell == 'R' else e - 1
                        
                        # Process litter collections
                        next_mask = mask
                        if cell == 'L':
                            next_mask |= (1 << litter_idx[(nr, nc)])
                            
                        # If we have collected all litter, return immediately (BFS guarantees shortest path)
                        if next_mask == target_mask:
                            return moves + 1
                            
                        # Only push to queue if we arrive with strictly greater energy than previous visits
                        if next_e > visited[nr][nc][next_mask]:
                            visited[nr][nc][next_mask] = next_e
                            q.append((nr, nc, next_mask, next_e))
            moves += 1
            
        return -1