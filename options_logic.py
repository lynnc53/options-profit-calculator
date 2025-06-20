import numpy as np 

def calculate_payoff(option_type, position, strike_price, premium, stock_prices):
    stock_prices = np.array(stock_prices ) # create a numpy array from stock_prices

    # calculate the payoff based on the option type 
    if option_type == 'call':
        payoff = np.maximum(stock_prices - strike_price, 0)
    elif option_type == 'put':
        payoff = np.maximum(strike_price - stock_prices, 0)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    # calculate the total payoff based on the position 
    if position == 'long':
        return payoff - premium 
    elif position == 'short':
        return -payoff + premium
    else:
        raise ValueError("Invalid position. Use 'long' or 'short'.")