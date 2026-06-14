def max_profit_dc(prices, left, right):
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    
    # Recursively find max profit in left and right halves
    left_profit = max_profit_dc(prices, left, mid)
    right_profit = max_profit_dc(prices, mid + 1, right)
    
    # Find minimum price in left half
    min_left = min(prices[left:mid+1])
    
    # Find maximum price in right half
    max_right = max(prices[mid+1:right+1])
    
    # Profit if buy in left, sell in right
    cross_profit = max_right - min_left
    
    return max(left_profit, right_profit, cross_profit)

def max_profit(prices):
    return max_profit_dc(prices, 0, len(prices) - 1)

# Example: 30 days of stock prices (shortened for demo)
prices = [100, 180, 260, 310, 40, 535, 695, 200, 150, 300,
          250, 400, 350, 600, 450, 700, 650, 800, 750, 900,
          850, 950, 920, 1000, 980, 1100, 1050, 1200, 1150, 1300]

profit = max_profit(prices)
print(f"Maximum profit: {profit}")