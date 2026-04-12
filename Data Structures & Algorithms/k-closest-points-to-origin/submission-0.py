class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l1 = [math.sqrt((x)**2 + (y)**2) for row in points for x, y in [row]]
        l3 = [[l1[i],points[i]] for i in range(len(l1))]

        heapq.heapify(l3)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(l3)[1])

        return ans