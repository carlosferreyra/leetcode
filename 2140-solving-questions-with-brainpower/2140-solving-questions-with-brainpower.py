
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}

        def solve(index):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]

            # Option 1: Solve the current question
            points, brainpower = questions[index]
            solve_next_index = index + brainpower + 1
            solve_points = points + solve(solve_next_index)

            # Option 2: Skip the current question
            skip_points = solve(index + 1)

            memo[index] = max(solve_points, skip_points)
            return memo[index]

        return solve(0)