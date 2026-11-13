"""
You are given two integer arrays nums and target of lengths n and m, respectively, where n <= m.

For each index i, consider sorting the suffix nums[i..n - 1] of the original array in non-increasing order.

Return an integer array ans of length m - n + 1, where ans[k] is the number of indices i for which the resulting array equals target[k..k + n - 1].

A suffix of an array is a subarray that begins at any index and extends to its end.

 

Example 1:

Input: nums = [2,2,3], target = [2,2,3,2,1,3,2,2]

Output: [1,1,0,0,0,1]

Explanation:

Sorting the suffix starting at indices 0, 1, and 2 produces [3, 2, 2], [2, 3, 2], and [2, 2, 3], respectively.

k = 0: [2, 2, 3] is produced by i = 2.
k = 1: [2, 3, 2] is produced by i = 1.
k = 2, 3, 4: None of the corresponding subarrays can be produced.
k = 5: [3, 2, 2] is produced by i = 0.
Therefore, the answer is [1, 1, 0, 0, 0, 1].

Example 2:

Input: nums = [5,6,5], target = [5,6,5,5,6,5]

Output: [2,1,0,2]

Explanation:

Sorting the suffix starting at index 0 produces [6, 5, 5], while starting at either index 1 or 2 produces [5, 6, 5].

k = 0: [5, 6, 5] is produced by i = 1 and i = 2.
k = 1: [6, 5, 5] is produced by i = 0.
k = 2: [5, 5, 6] cannot be produced.
k = 3: [5, 6, 5] is produced by i = 1 and i = 2.
Therefore, the answer is [2, 1, 0, 2].

 

Constraints:

n == nums.length
m == target.length
1 <= n <= m <= 105
1 <= nums[i], target[i] <= 105


"""
class Solution:
    def countSuffix(self, nums, target):

        n, m = len(nums), len(target)

        a = nums + [0] + target
        z = [0] * len(a)
        l = r = 0

        for i in range(1, len(a)):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])

            while i + z[i] < len(a) and a[z[i]] == a[i + z[i]]:
                z[i] += 1

            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1

        freq = [0] * 100001
        bad = 0

        def update(x, d):
            nonlocal bad

            old = freq[x]
            freq[x] += d

            if old == 0 and freq[x] != 0:
                bad += 1
            elif old != 0 and freq[x] == 0:
                bad -= 1

        for x in nums:
            update(x, 1)

        for x in target[:n]:
            update(x, -1)

        last = [-1] * m
        prev = -1

        for i in range(m):
            if i > 0 and target[i - 1] < target[i]:
                prev = i - 1
            last[i] = prev

        ans = [0] * (m - n + 1)

        for k in range(m - n + 1):

            if k > 0:
                update(target[k - 1], 1)
                update(target[k + n - 1], -1)

            if bad != 0:
                continue

            p = min(n, z[n + 1 + k])

            q = max(0, last[k + n - 1] - k + 1)

            ans[k] = max(0, min(p, n - 1) - q + 1)

        return ans

nums = [5,6,5]
target = [5,6,5,5,6,5]


a1 = Solution()
print(a1.countSuffix(nums , target))
