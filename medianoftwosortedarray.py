class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         # we need to have nums1 as smaller in length
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n = len(nums1)
        m = len(nums2)
        min_idx = 0
        max_idx = n
        
        while min_idx <= max_idx:
            
            # find partition points of both
            # such that lefthalf of both equals or greater or smaller by 1 to righthalf of both
            # i = partition point of nums1 and j = partition point of nums2
            # so basically i - 1 is last element of leftHalf of nums1 
            # j - 1 is last element of leftHalf of nums2
            i = int((min_idx + max_idx)/2)
            j = int((n + m + 1)/2 - i)
            
            # nums2's left half is greater than nums1's right half
            if i < n and j > 0 and nums2[j-1] > nums1[i]:
                min_idx = i + 1
            
            # nums1's left half is greater than nums2's right half
            elif i > 0 and j < m and nums1[i-1] > nums2[j]:
                max_idx = i - 1
            
            # nums1's and nums2's lefthalf are smaller than their righthalf
            # that means we found point where medians are
            else:
                
                # if i == 0 that means nums1 left half is empty
                if i == 0:
                    median = nums2[j - 1]
                # if j == 0 that means nums2 left half is empty
                elif j == 0:
                    median = nums1[i - 1]
                else:
                    median = max(nums1[i - 1], nums2[j - 1])
                break
        
        # to check even and odd cases
        if (n + m) % 2: # that means odd
            return median
        
        # even and check edge cases
        if i == n:
            return (median + nums2[j])/2.0
        elif j == m:
            return (median + nums1[i])/2.0
        
        return (median + min(nums1[i], nums2[j]))/2.0