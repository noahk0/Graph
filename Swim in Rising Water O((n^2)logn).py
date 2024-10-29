def swimInWater(self, grid: List[List[int]]) -> int:
    res, candidate, grid[0][0] = max(grid[0][0], grid[-1][-1]), [[grid[0][0], 0, 0]], None
        
    while candidate:
        depth, x, y = heappop(candidate)
        res = max(res, depth)

        for i, j in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:
            if 0 <= i < len(grid) and 0 <= j < len(grid) and grid[i][j] != None:
                if i == j == len(grid) - 1:
                    return res

                heappush(candidate, [grid[i][j], i, j])
                grid[i][j] = None

    return res
