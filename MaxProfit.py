def MaxProfit(A):
    # A[k] = price of stock share on day k. A[Q] - A[P] = net profit/loss experienced between days P and Q, where P < Q
    # find maximum profit
    max_profit = 0
    min_day = 200000 # this is given as greatest possible value of any array element
     
    for day in A:
        min_day = min(min_day, day)
        max_profit = max(max_profit, day-min_day)
     
    return max_profit
