import os
import time
import ctypes
import subprocess
import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt

# Resize the terminal window for Mac OS
if os.name == "posix":
    subprocess.run(['resize', '-s', '22', '72'])

# Resize the terminal window for Windows
if os.name == "nt":
    # Windows
    os.system("mode con: cols=72 lines=22")

# Rename terminal window
ctypes.windll.kernel32.SetConsoleTitleW("Power to the Players")

# GameStop Banner
banner = """
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████   ██████ ▄▄▄█████▓ ▒█████   ██▓███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██░  ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   ░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██░ ██▓▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▄█▓▒ ▒
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒▒██████▒▒  ▒██▒ ░ ░ ████▓▒░▒██▒ ░  ░
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░░ ░▒  ░ ░    ░      ░ ▒ ▒░ ░▒ ░     
░ ░   ░   ░   ▒   ░      ░      ░   ░  ░  ░    ░      ░ ░ ░ ▒  ░░       
      ░       ░  ░       ░      ░  ░      ░               ░ ░           
                                                                        
                                                        By: Wayahlife
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""

# Print the banner to the console
print(banner)

# Get the stock data for GameStop
gme = yf.Ticker("GME")

# Option Menu
print("1. Get the current price of GME.")
print("2. Get the historical data of GME.")
print("3. Plot the historical data of GME.")
print("4. View the GME DD library.")
print("5. Visit HQ r/Superstonk.")
print("6. Exit\n")

# Get the user's choice
choice = int(input("Enter your choice: "))

# Handle the user's choice
try:
    if choice == 1:
        # Get the current price of the stock
        os.system("start python3 price.py")
        os.system("python3 main.py")

    elif choice == 2:

        # Get the historical data for the stock
        data = gme.history(period="1y")
        print(data)

        # Option
        print("\nSelect another option? (y/n)")
        option = input("Enter an option: ")
        if option == "y" or option == "Y":
            os.system("python3 main.py")

    elif choice == 3:

        # Get the historical data for the stock
        data = gme.history(period="1y")

        # Plot the data
        mpf.plot(data, type="candle", style="charles", volume=True, title="GameStop (GME)")

        # Show the plot
        plt.show()
        os.system("python3 main.py")
    
    elif choice == 4:
        # Open the subreddit in a new window
        os.system("start http://www.gme.fyi")
        os.system("python3 main.py")

    elif choice == 5:

        # Open the subreddit in a new window
        os.system("start https://www.reddit.com/r/Superstonk/")
        os.system("python3 main.py")
    
    elif choice == 6:
        # Exit the program
        print("""\n
        Hedgies R' Fuk. 
        Ken Griffin lied under oath. 
        DTCC committed international securities fraud.
        DRS your shares.\n""")
        time.sleep(5)
    os.system("cls")
    exit()

except (KeyboardInterrupt, SystemExit, ValueError, TypeError):
    print("\nExiting... Hedgies R' Fuk.\n")
