class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = [-1] * len(nums1)
        stack = []
        num_dict = defaultdict(int)

        for i in range(len(nums1)):
            num_dict[nums1[i]] = i
        for i in range(len(nums2)):
            val = nums2[i]

            while stack and val > stack[-1]:
                idx = num_dict.get(stack.pop())
                if idx is not None:
                    ans[idx] = val

            stack.append(val)

        return ans
