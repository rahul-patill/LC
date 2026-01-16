class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def setZero(list_number, index_number,m,n):
            # new_list = [0]*m
            # matrix[list_number] = new_list

            for i in range(0,m):
                matrix[list_number][i] = 0

            for i in range(0,n):
                matrix[i][index_number] = 0

        index_of_zero = []
        m = len(matrix[0])
        n = len(matrix)
        print(m,n)

        for i in range(0,n):
            for j in range(0, m):
                if matrix[i][j] == 0:
                    index_of_zero.append([i,j])
        print(index_of_zero)

        for i in index_of_zero:
            list_number = i[0]
            index_number = i[1]
            setZero(list_number, index_number,m,n)


        