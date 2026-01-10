class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0  # down
        j = len(matrix[0]) - 1  # right

        n = len(matrix)  # column/down length
        m = len(matrix[0]) # row/right length

        while (i >= 0 and i < n) and (j >= 0 and j < m):

            if matrix[i][j] == target:
                return True

            elif target < matrix[i][j]:
                j -= 1

            elif matrix[i][j] < target:
                i += 1

        return False