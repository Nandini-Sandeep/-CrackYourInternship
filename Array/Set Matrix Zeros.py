class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows=set(); cols=set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):
            if i in rows:
                matrix[i] = [0]*n
                continue
            for j in range(n):
                if j in cols:
                    matrix[i][j]=0
                    
