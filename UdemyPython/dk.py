class Solution(object):
    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1 + nums2
        print(((nums1).sort()).lstrip(0))

nums1 = [2,4,6,0,0,0]  
nums2 = [1,3,5]     
merge(nums1,3,nums2,3)
        