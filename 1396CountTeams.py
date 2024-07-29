class Solution:
    def numTeams(self, rating: List[int]) -> int:
        length = len(rating)
        result = 0

        #loop through each soldier apart from the first and last
        for soldier in range(1, length-1):
            current_rating = rating[soldier]
            left_low = left_high = right_low = right_high = 0

            #count soldiers ratings each side of the middle one
            for i in range(soldier):
                if rating[i] < current_rating:
                    left_low += 1
                else:
                    left_high += 1

            for i in range(soldier + 1, length):
                if rating[i] < current_rating:
                    right_low += 1
                else:
                    right_high += 1

            #tally up the combinations. If there are 0 to one side then it would be impossible for that soldier to be valid. 
            result += left_low * right_high + left_high * right_low

        return result