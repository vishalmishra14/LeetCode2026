"""
973. K Closest Points to Origin
Medium
Topics
premium lock icon
Companies
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104

"""
from typing import List
import heapq

class Solution:
    # Sorting with Custom Comparator
    def euclidean_distance(self, point:  List[int]) -> float:
        return (point[0] ** 2 + point[1] ** 2) ** 0.5
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=self.euclidean_distance)
        return points[:k] 

    # # Sorting with Lambda Function
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     points.sort(key=lambda p: p[0] **2 + p[1] ** 2)
    #     return points[:k]

    # # Using Min-Heap
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     min_heap = []
    #     for point in points:
    #         distance = point[0] ** 2 + point[1] ** 2
    #         min_heap.append([distance, point])
    #     heapq.heapify(min_heap)
    #     return [heapq.heappop(min_heap)[1] for _ in range(k)]

    # # Using Quickselect Algorithm
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     euclidean_distance = lambda p: p[0] ** 2 + p[1] ** 2
    #     def partition(self, left: int, right: int) -> int:
    #         pivotIdx = right
    #         pivotDist = euclidean_distance(points[pivotIdx])
    #         storeIdx = left
    #         for i in range(left, right): 
    #             if euclidean_distance(points[i]) < pivotDist:
    #                 points[storeIdx], points[i] = points[i], points[storeIdx]
    #                 storeIdx += 1
    #         points[storeIdx], points[pivotIdx] = points[pivotIdx], points[storeIdx]
    #         return storeIdx
    #     L, R = 0, len(points) - 1
    #     pivot = len(points)
    #     while pivot != k:
    #         pivot = partition(self, L, R)
    #         if pivot < k:
    #             L = pivot + 1
    #         else:
    #             R = pivot - 1
    #     return points[:k]
        
        
s = Solution()
print(s.kClosest([[1,3],[-2,2]], 1))  #[[-2,2]]
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))  #[[3,3],[-2,4]] or [[-2,4],[3,3]]
