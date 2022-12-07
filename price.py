import os
import yfinance as yf

# Resize the terminal window
if os.name == "nt":
    # Windows
    os.system("mode con: cols=35 lines=15")

gme = yf.Ticker("GME")

try:
    while True:
        info = gme.info
        price = info["regularMarketPrice"]
        print(f"The current price of GME is ${price}")
except KeyboardInterrupt:
    print("Exiting...")
