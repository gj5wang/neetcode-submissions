class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #basic logic:
        #sortedpiles = sorted(piles)
        sortedpiles = sorted(piles)
        left = 1
        right = sortedpiles[len(sortedpiles) - 1]
        #so basically max k is right min k is left
        #binary sorting
        while(left < right):
            hours = 0
            mid = (left + right) // 2
            for i in range(len(sortedpiles)):
                if sortedpiles[i] % mid == 0:
                    hours = hours + sortedpiles[i] // mid
                elif mid < sortedpiles[i]:
                    hours = hours + sortedpiles[i] // mid + 1
                else:
                    hours = hours + 1
            if hours > h:
                left = mid + 1
            elif hours <= h:
                right = mid
        #find the hours required to eat in mid speed
        #if hours > h, everything below mid is too slow
        # left = mid + 1
        #if hours <= h, then k could be the answer but there might be a smaller option
        # right = mid

        return left
        #return left(the mid right before left = right)