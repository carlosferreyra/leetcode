import collections
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """
        Counts the number of good subarrays using a sliding window approach.

        A subarray is good if it has at least k pairs (i, j) such that
        i < j and nums[i] == nums[j].

        Args:
            nums: The input integer array.
            k: The minimum number of pairs required for a subarray to be good.

        Returns:
            The total number of good subarrays.
        """
        n = len(nums)
        l = 0  # Left pointer of the sliding window
        res = 0 # Result: total count of good subarrays
        current_pairs = 0 # Number of pairs in the current window [l, r]
        counts = collections.defaultdict(int) # Frequency map for elements in the window

        # Iterate through the array with the right pointer 'r'
        for r in range(n):
            num_r = nums[r]

            # --- Expand Window (Add nums[r]) ---
            # Adding nums[r] creates 'counts[num_r]' new pairs
            # with the existing occurrences of num_r in the window [l, r).
            current_pairs += counts[num_r]
            counts[num_r] += 1 # Increment the count of num_r in the window

            # --- Shrink Window (if condition met) ---
            # While the current window [l, r] has at least k pairs,
            # it means this window and potentially shorter windows ending at r are good.
            # We shrink the window from the left to find the boundary.
            while current_pairs >= k:
                num_l = nums[l]

                # Removing nums[l] breaks 'counts[num_l] - 1' pairs.
                # First, decrement the count.
                counts[num_l] -= 1
                # Then, subtract the remaining count (which represents the broken pairs).
                current_pairs -= counts[num_l]

                # If count becomes 0, it's effectively removed from defaultdict's perspective
                # No explicit deletion needed, though possible for minor space optimization.
                # if counts[num_l] == 0:
                #    del counts[num_l]

                l += 1 # Move the left pointer to shrink the window

            # --- Count Subarrays ---
            # At this point, the window [l, r] has < k pairs (or l was just incremented).
            # This means any subarray ending at 'r' and starting at an index 'i'
            # where 0 <= i < l *must* have had >= k pairs (because we only stopped
            # shrinking when the count dropped below k).
            # The number of such starting indices is 'l'.
            # So, we add 'l' to the total count of good subarrays.
            res += l

        return res