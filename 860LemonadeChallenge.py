class Solution:
    def lemonadeChange(self, bills) -> bool:
        """
        This function takes in a list of bills and returns whether the lemonade stand
        can make change for all of the bills or not. The stand starts with an empty
        register and each bill must be paid in order.

        The problem is solved by keeping track of the number of 5 and 10 dollar bills
        in the register. When a 10 dollar bill is given, it is immediately exchanged
        for a 5 dollar bill (if one is available). When a 20 dollar bill is given, it
        can be exchanged for 3 5 dollar bills or one 10 dollar bill and one 5 dollar
        bill. If the register does not have enough money to make change, the function
        returns false.
        """
        # The first bill must be a 5 dollar bill
        if bills[0] != 5:
            return False

        # Initialize the number of 5 and 10 dollar bills in the register
        change5, change10 = 0, 0

        # Iterate over each bill in the list
        for bill in bills:
            # If the bill is a 5 dollar bill, increment the count in the register
            if bill == 5:
                change5 += 1
            # If the bill is a 10 dollar bill, decrement the count of 5 dollar bills
            # and increment the count of 10 dollar bills
            elif bill == 10:
                if change5 > 0: 
                    change5 -= 1
                    change10 += 1
                else:
                    return False
            # If the bill is a 20 dollar bill, either exchange it for 3 5 dollar bills
            # or one 10 dollar bill and one 5 dollar bill
            else: 
                if change10 > 0 and change5 > 0:
                    change10 -= 1
                    change5 -= 1
                elif change5 > 2:
                    change5 -=3
                else:
                    return False
        # If the function has not returned False yet, then the lemonade stand can make
        # change for all of the bills
        return True
