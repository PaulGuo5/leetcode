class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis = sorted(points, key = lambda x: x[0]**2 + x[1]**2)
        return dis[:K]