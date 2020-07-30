class Solution:
    def oddCells(self, rows: int, col: int, indices):
        
        matrix = [[0 for i in range(col)] for j in range(rows)]
        count = 0

        for index in indices:
            r, c = index
            # print('r = ', r ,  'c = ', c)

            #ROWS
            for i in range(col):
                matrix[r][i] += 1
                # print('after row ops = ', matrix)
            
            #Columns
            for j in range(rows):
                matrix[j][c] += 1
                # print('after col ops = ', matrix)
            
            # print('---------------------------------------')
        

        for i in matrix:
            for j in i:
                if j % 2 != 0:
                    count += 1

        return count

m = Solution()
print(m.oddCells(2, 3, [[0, 1], [1, 1]]))