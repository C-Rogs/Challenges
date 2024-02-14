def maxProfit(prices):

    start, end, max_profit = 0, 1, 0 
    while end < len(prices):
        profit = prices[end] - prices[start]
        if prices[start] < prices[end]:
            max_profit = max(profit, max_profit)
        else: 
            start = end 
        end += 1
    return max_profit

def test_maxProfit():
    assert maxProfit([7,1,5,3,6,4]) == 5, "Test case 1 failed"
    assert maxProfit([7,6,4,3,1]) == 0, "Test case 2 failed"
    assert maxProfit([1,2,3,4,5]) == 4, "Test case 3 failed"
    assert maxProfit([2,4,1]) == 2, "Test case 4 failed"
    assert maxProfit([3,2,6,5,0,3]) == 4, "Test case 5 failed"
    print("All test cases passed")

test_maxProfit()