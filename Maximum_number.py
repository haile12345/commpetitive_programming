class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        # sort array in descending order
        piles.sort(reverse=True)
        # keep track of total
        total: int = 0
        # value of n
        n: int = int(len(piles)/3)

        i: int = 0
        while n > 0:
            # second alternate element
            if i % 2 == 1:
                # adding to total
                total += piles[i]
                # decrementing n
                n -= 1
            i += 1
        return total
