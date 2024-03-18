class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

if __name__ == "__main__":
    s = Solution()


    print(s.reverseBits(0)) # Expected output: 0

    print(s.reverseBits(2**32 - 1)) # Expected output: 2**32 - 1

    print(s.reverseBits(43261596)) # Expected output: 964176192

    print(s.reverseBits(4294967293)) # Expected output: 3221225471