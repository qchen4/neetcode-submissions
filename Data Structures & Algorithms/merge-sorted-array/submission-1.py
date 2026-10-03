class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
     
        while i < m+j and j < n:
    
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1[i +1 : m +j +1] = nums1[i: m+j]
                nums1[i] = nums2[j]
                i += 1
                j += 1
        if j < n:
            nums1[m+j::] = nums2[j:n]


                    


