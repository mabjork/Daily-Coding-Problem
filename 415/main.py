import time
fee = 2

def calculate_optimal_purchases(stock_prices, fee = fee):
    profit = 0
    num_transactions = 0
    buy_index = 0
    while buy_index < len(stock_prices) - 1:
        buy_price = stock_prices[buy_index]
        highest_sell_index = None
        highest_sell_price = -1
        for sell_index in range(buy_index, len(stock_prices)):
            sell_price = stock_prices[sell_index]
            if(sell_price > highest_sell_price and sell_price - buy_price > fee):
                highest_sell_price = sell_price
                highest_sell_index = sell_index
            if(sell_price + fee < highest_sell_price):
                break
        
        if (highest_sell_index == None):
            buy_index += 1
        else:
            buy_index = highest_sell_index + 1
            profit += highest_sell_price - buy_price
            num_transactions += 1
    return profit - num_transactions * fee

prices = [1, 3, 2, 8, 4, 10]

print(calculate_optimal_purchases(prices))




