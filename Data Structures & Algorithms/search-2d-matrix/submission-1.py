class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1

        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.searchRow(matrix[mid],target)
            elif target > matrix[mid][-1]:
                l=mid+1
            else:
                r=mid-1
                
        return False

    def searchRow(self, row, target):
        l=0
        r=len(row)-1
        while l <= r:
            mid = (l+r)//2
            if target==row[mid]:
                return True
            elif target > row[mid]:
                l=mid+1
            else:
                r=mid-1
        return False
