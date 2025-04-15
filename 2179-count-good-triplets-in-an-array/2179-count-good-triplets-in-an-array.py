class Solution:
    """
    Solves the LeetCode problem "Count Good Triplets in an Array".
    A triplet (x, y, z) is good if x, y, z appear in increasing order of indices
    in both nums1 and nums2. The values x, y, z are from the range [0, n-1].
    """

    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Counts the number of good triplets using Fenwick Trees (BIT).
        The core idea is to transform the problem into counting triplets (i, j, k)
        such that i < j < k and p[i] < p[j] < p[k], where p is a derived array
        based on the indices of elements in nums1 and nums2.

        Args:
            nums1: The first permutation of [0, ..., n-1].
            nums2: The second permutation of [0, ..., n-1].

        Returns:
            The total count of good triplets.
        """
        n = len(nums1)
        # A triplet requires at least 3 elements.
        if n < 3:
            return 0

        # Implementation of Fenwick Tree (Binary Indexed Tree) nested inside the method
        class FenwickTree:
            """
            A Fenwick Tree (Binary Indexed Tree) supports point updates and prefix sum queries
            in O(log n) time complexity.
            It uses 1-based indexing internally for easier calculation of parent/next nodes.
            The tree handles 0-based indices for updates and queries externally.
            """

            def __init__(self, size: int):
                """
                Initializes the Fenwick Tree.
                Args:
                    size: The maximum value (exclusive) the tree will handle indices for.
                          The tree will effectively handle indices from 0 to size-1.
                          The internal array size is size + 1 for 1-based indexing.
                """
                # Initialize tree with zeros, size+1 for 1-based indexing
                self.tree = [0] * (size + 1)
                # Store the effective size (number of elements it can represent, 0 to size-1)
                self.size = size

            def update(self, i: int, delta: int) -> None:
                """
                Adds delta to the element at index i (0-based).
                Args:
                    i: The 0-based index to update. Should be in range [0, size-1].
                    delta: The value to add at index i.
                """
                # Convert to 1-based index for internal tree structure
                i += 1
                # Traverse up the tree, updating relevant nodes
                while i <= self.size:
                    self.tree[i] += delta
                    # Move to the next index that includes the current index's range
                    # i & (-i) gives the value of the least significant bit set in i
                    i += i & (-i)

            def query(self, i: int) -> int:
                """
                Queries the prefix sum up to index i (inclusive, 0-based).
                This calculates the sum of elements from index 0 to i.
                Args:
                    i: The 0-based index up to which the sum is required. Should be in range [-1, size-1].
                       If i is -1, the sum is 0.
                Returns:
                    The prefix sum sum(arr[0...i]).
                """
                # Handle query for index -1 (e.g., when querying for elements < 0)
                if i < 0:
                    return 0
                # Convert to 1-based index for internal tree structure
                i += 1
                s = 0
                # Traverse down the tree, summing relevant node values
                while i > 0:
                    s += self.tree[i]
                    # Move to the parent index which covers a prefix range ending before i
                    i -= i & (-i)
                return s

        # Create a mapping from value to its index in nums1 for O(1) lookup.
        # pos1[value] = index in nums1
        pos1 = {val: i for i, val in enumerate(nums1)}

        # Create array `p` where p[idx1] = idx2.
        # This array `p` maps the position in `nums1` to the position in `nums2`.
        p = [0] * n
        for idx2, val in enumerate(nums2):
            idx1 = pos1[val]
            p[idx1] = idx2

        # Calculate `less_left[j]` for all `j` using a Fenwick tree (`bit1`).
        less_left = [0] * n
        bit1 = FenwickTree(n)
        for j in range(n):
            less_left[j] = bit1.query(p[j] - 1)
            bit1.update(p[j], 1)

        # Calculate `greater_right[j]` for all `j` using another Fenwick tree (`bit2`).
        greater_right = [0] * n
        bit2 = FenwickTree(n)
        for j in range(n - 1, -1, -1):
            greater_right[j] = bit2.query(n - 1) - bit2.query(p[j])
            bit2.update(p[j], 1)

        # Calculate the final answer by summing the products.
        ans = 0
        for j in range(n):
            ans += less_left[j] * greater_right[j]

        return ans