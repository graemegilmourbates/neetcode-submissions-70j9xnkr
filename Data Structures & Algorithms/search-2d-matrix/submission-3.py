class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i=0;
        while(target>matrix[i][m-1]):
            i += 1
            if(i>=n):
                return False
        if(i<0):
            return False
        j=0;
        while(j<m):
            if(matrix[i][j]==target):
                return True
            j+=1
        return False
