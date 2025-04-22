import sys

sys.setrecursionlimit(20000)  # Increase recursion depth for combinations if needed

MOD = 10**9 + 7

def power(a, b):
    """Computes (a^b) % MOD"""
    res = 1
    a %= MOD
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return res

def modInverse(n):
    """Computes modular inverse of n modulo MOD using Fermat's Little Theorem"""
    return power(n, MOD - 2)

def combinations(n, k, fact, invFact):
    """Computes (n choose k) % MOD using precomputed factorials and inverse factorials"""
    if k < 0 or k > n:
        return 0
    return (fact[n] * invFact[k] % MOD * invFact[n - k] % MOD)

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        """
        Calculates the number of distinct ideal arrays of length n.

        An ideal array arr of length n satisfies:
        - 1 <= arr[i] <= maxValue for 0 <= i < n
        - arr[i] is divisible by arr[i - 1] for 0 < i < n

        Args:
            n: The length of the ideal array.
            maxValue: The maximum allowed value for elements in the array.

        Returns:
            The number of distinct ideal arrays modulo 10^9 + 7.
        """
        # Precompute factorials and modular inverses
        # Maximum value for n_ck is e_p(v) + n - 1, where e_p(v) <= log_p(maxValue)
        # Max e_p(v) is around log_2(maxValue).
        # So max N in C(N, K) is around log_2(maxValue) + n - 1.
        # For maxValue = 10^4, log_2(10^4) approx 13.
        # Max N approx 13 + 10^4 - 1 = 10012. Let's use maxValue + n for safety.
        max_fact = maxValue + n + 5 # Add a buffer
        fact = [1] * max_fact
        invFact = [1] * max_fact
        for i in range(2, max_fact):
            fact[i] = (fact[i - 1] * i) % MOD
            invFact[i] = modInverse(fact[i])

        # Sieve for smallest prime factor to efficiently find prime factorization
        spf = [i for i in range(maxValue + 1)]
        for i in range(2, int(maxValue**0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, maxValue + 1, i):
                    if spf[j] == j:  # If spf[j] is still j, it means j is not marked by a smaller prime
                        spf[j] = i

        total_count = 0
        for v in range(1, maxValue + 1):
            # For each number v from 1 to maxValue, consider it as the last element of the ideal array.
            # The number of ideal arrays ending with v is the product of the number of ways
            # to form non-decreasing sequences of powers for each prime factor of v.

            current_v = v
            term = 1  # Represents the product of combinations for prime factors of v

            # Prime factorize v
            while current_v > 1:
                p = spf[current_v]
                count = 0  # Power of prime p in v
                while current_v % p == 0:
                    count += 1
                    current_v //= p

                # Number of non-decreasing sequences of powers of prime p of length n,
                # ending at 'count'.
                # This is equivalent to choosing n-1 intermediate powers from 0 to 'count'.
                # Using stars and bars: C(count + n - 1, n - 1)
                term = (term * combinations(count + n - 1, n - 1, fact, invFact)) % MOD

            total_count = (total_count + term) % MOD

        return total_count