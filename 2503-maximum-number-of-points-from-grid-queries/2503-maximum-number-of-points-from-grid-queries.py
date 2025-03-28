import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        queries_with_index = sorted([(q, i) for i, q in enumerate(queries)])
        answer = [0] * len(queries)
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        points = 0
        query_index = 0

        while query_index < len(queries):
            query, original_index = queries_with_index[query_index]

            while heap and heap[0][0] < query:
                val, row, col = heapq.heappop(heap)
                points += 1

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in visited:
                        heapq.heappush(heap, (grid[new_row][new_col], new_row, new_col))
                        visited.add((new_row, new_col))

            answer[original_index] = points
            query_index += 1

        return answer