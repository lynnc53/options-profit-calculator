from options_logic import calculate_payoff
import matplotlib.pyplot as plt

# example test case:
stock_prices = list(range(40,131)) # stock prices from 40 to 130
strike_price = 100
premium = 15 

# call function and choose option type and position 
payoff = calculate_payoff('call', 'long', strike_price, premium, stock_prices)

plt.plot(stock_prices, payoff, label='Long Call Payoff')
plt.axhline(0, color='black', linewidth=0.5) # draw horizontal line at zero
plt.axvline(strike_price, color='red', linestyle='--', label='Strike Price') # draw vertical line at strike price
plt.title('Options Payoff Test')
plt.xlabel('Stock Price at Expiration')
plt.ylabel('Profit / Loss')
plt.legend()
plt.grid(True)
# save the plot as a png file 
plt.savefig('test_case/long_call_payoff.png') 
plt.show()
