import os
import time
import ctypes
import yfinance as yf

# Resize the terminal window
if os.name == "nt":
    # Windows
    os.system("mode con: cols=77 lines=15")

# Rename terminal window
ctypes.windll.kernel32.SetConsoleTitleW("GME Historical Data - [1 Year]")

gme = yf.Ticker("GME")

# Get the historical data for the stock
data = gme.history(period="1y")
print(data)

# Keep window open
time.sleep(5000)