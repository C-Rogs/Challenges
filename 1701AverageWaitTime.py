class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        wait_total = customers[0][1]
        finish_time = customers[0][0] + customers[0][1]

        for i in range(1,len(customers)):
            arrival_time = customers[i][0]
            cook_time = max(arrival_time, finish_time)
            finish_time = cook_time + customers[i][1]
            wait_total += finish_time - arrival_time

        return wait_total / len(customers)