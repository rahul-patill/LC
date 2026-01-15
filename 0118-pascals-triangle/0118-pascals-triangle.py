class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_ans = [[1]]
        
        j = 1
        while j <= numRows - 1:
            current_row = []
            previous_row = final_ans[-1]

            for i in range(0, j + 1):
                if (i == 0) or (i == j):
                    current_row.append(1)
                else:
                    current_row.append((previous_row[i - 1]) + (previous_row[i]))

            final_ans.append(current_row)
            previous_row = current_row
            j += 1

        return final_ans
