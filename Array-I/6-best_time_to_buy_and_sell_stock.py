# ============================================================
# BEST TIME TO BUY AND SELL STOCK
# ============================================================
#
# Problem:
#
# prices[i] represents the stock price on day i.
#
# You may:
# - Buy once
# - Sell once
#
# Buy must happen before Sell.
#
# Return the maximum possible profit.
#
# Example:
#
# prices = [7,1,5,3,6,4]
#
# Buy  at 1
# Sell at 6
#
# Profit = 6 - 1 = 5
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Treat every day as a potential SELL day.
#
# Then ask:
#
# "What is the minimum stock price seen before today?"
#
# Example:
#
# prices = [7,1,5,3,6,4]
#
# At price = 6:
#
# min_price_so_far = 1
#
# profit = 6 - 1 = 5
#
# Therefore:
#
# profit = current_price - min_price_so_far
#
# Maintain:
#
# - min_price
# - max_profit
#
# This directly gives the O(N) solution.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# Try every Buy-Sell pair and keep the maximum profit.
#
# TIME  : O(N²)
# SPACE : O(1)
#
# ============================================================

def max_profit_brute(prices):

    n = len(prices)

    max_profit = 0

    for buy_day in range(n):

        for sell_day in range(buy_day + 1, n):

            profit = prices[sell_day] - prices[buy_day]

            max_profit = max(max_profit, profit)

    return max_profit


# ============================================================
# 2. OPTIMAL APPROACH
# ============================================================
#
# Maintain:
#
# min_price  -> cheapest price seen so far
# max_profit -> best profit found so far
#
# For every price:
#
# profit = current_price - min_price
#
# Update:
#
# 1. max_profit
# 2. min_price
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================

def max_profit_optimal(prices):

    min_price = float("inf")

    max_profit = 0

    for price in prices:

        min_price = min(min_price, price)

        profit = price - min_price

        max_profit = max(max_profit, profit)

    return max_profit


# ============================================================
# 3. OPTIMAL + BUY/SELL DAYS
# ============================================================
#
# Follow-Up:
#
# Return:
# - Maximum Profit
# - Buy Day
# - Sell Day
#
# Track:
#
# min_price
# min_price_day
#
# Whenever a better profit appears,
# update buy_day and sell_day.
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================

def max_profit_with_days(prices):

    min_price = float("inf")
    min_price_day = 0

    max_profit = 0

    buy_day = -1
    sell_day = -1

    for day in range(len(prices)):

        if prices[day] < min_price:

            min_price = prices[day]
            min_price_day = day

        profit = prices[day] - min_price

        if profit > max_profit:

            max_profit = profit

            buy_day = min_price_day
            sell_day = day

    return max_profit, buy_day, sell_day


# ============================================================
# EDGE CASE
# ============================================================
#
# prices = [7,6,5,4,3]
#
# No profitable transaction exists.
#
# Answer = 0
#
# Meaning:
# Don't buy at all.
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

prices = [7, 1, 5, 3, 6, 4]

print("================================================")
print("INPUT STOCK PRICES")
print("================================================")

print(prices)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Maximum Profit =",
    max_profit_brute(prices)
)

print()

print("================================================")
print("2. OPTIMAL APPROACH")
print("================================================")

print(
    "Maximum Profit =",
    max_profit_optimal(prices)
)

print()

print("================================================")
print("3. OPTIMAL + BUY/SELL DAYS")
print("================================================")

profit, buy_day, sell_day = max_profit_with_days(prices)

print("Maximum Profit =", profit)

print(
    "Buy Day        =",
    buy_day,
    "(Price =", prices[buy_day], ")"
)

print(
    "Sell Day       =",
    sell_day,
    "(Price =", prices[sell_day], ")"
)

print()

print("================================================")
print("DECREASING PRICES TEST")
print("================================================")

prices2 = [7, 6, 5, 4, 3]

print("Prices         =", prices2)

print(
    "Maximum Profit =",
    max_profit_optimal(prices2)
)