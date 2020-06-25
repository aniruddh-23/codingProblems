class Solution:
    def matrixSqSum(self,mat):
        sum_mat=[[0 for i in range(len(mat[0])+1)] for j in range((len(mat)+1))]
        #sum_mat[1][1]=mat[0][0]
        """
        for col in range(1,len(mat[0])):
            sum_mat[0][col]=sum_mat[0][col-1]+mat[0][col]
        for row in range(1,len(mat)):
            sum_mat[row][0]=sum_mat[row-1][0]+mat[row][0]
        """
        for row in range(1,len(mat)+1):
            for col in range(1,len(mat[0])+1):
                sum_mat[row][col]=sum_mat[row-1][col]+sum_mat[row][col-1]-sum_mat[row-1][col-1]+mat[row-1][col-1]
        return sum_mat
    def matSum(self,beg,end,sum_mat):
        rowB,colB = beg[0]+1,beg[1]+1
        rowE,colE = end[0]+1,end[1]+1
        
        return sum_mat[rowE][colE]-sum_mat[rowB-1][colE]-sum_mat[rowE][colB-1]+sum_mat[rowB-1][colB-1]
    
    def matrixBlockSum(self, mat, K):
        sum_mat=self.matrixSqSum(mat)
        M=len(mat)
        N=len(mat[0])
        for row in range(0,len(mat)):
            for col in range(0,len(mat[0])):
                beg = (row-K if row-K>0 else 0,col-K if col-K>0 else 0)
                end = (row+K if row+K<M else M-1,col+K if col+K<N else N-1)
                mat[row][col]=self.matSum(beg,end,sum_mat)
        return mat
        
        