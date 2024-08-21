class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2, 3, 5]
        nextup = [2, 3, 5]
        increase = [1, 1, 1]
        result = [1]

        for x in range(1,n):
            smallest = min(nextup)
            result.append(smallest)

            for i in range(3):
                if nextup[i] == smallest:
                    increase[i] += 1
                    nextup[i] = primes[i] * result[increase[i] - 1]

        return result[-1]