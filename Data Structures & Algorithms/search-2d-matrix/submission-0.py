class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l2 = []
        for row in matrix:
            for x in row:
                l2.append(x)
        lo,hi = 0,len(l2)-1
        while lo<=hi:
            mid = (lo + hi) //2
            if l2[mid] == target:
                return True
            elif l2[mid]<target:
                lo = mid+1
            else:
                hi = mid-1
        return False