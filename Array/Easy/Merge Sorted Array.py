class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # m in nums1; n in nums2
        L = []
        i=0; j=0
        while (i<m and j<n):
            a = nums1[i]; b=nums2[j];
            print(a, "vs", b)
            if nums1[i]<nums2[j]:
                i+=1;
            else:
                nums1.insert(i,nums2[j])
                nums1.pop(); m+=1;
                j+=1;
        # for remaining terms in nums2
        for a in nums2[j:]:
            nums1[i]=a
            i+=1
        
        nums1 = L


        
