import os

def stock_portfolio_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 150,
        "MSFT": 400,
        "AMZN": 175
    }
    
    portfolio = []
    total_value = 0
    
    print("Task 2: Stock Portfolio Tracker")
    print("Available stocks: " + ", ".join(stock_prices.keys()))
    
    while True:
        symbol = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        
        if symbol == 'DONE':
            break
            
        if symbol in stock_prices:
            try:
                quantity = int(input("Enter quantity for " + symbol + ": "))
                price = stock_prices[symbol]
                investment = price * quantity
                total_value += investment
                
                portfolio.append(symbol + ": " + str(quantity) + " shares at $" + str(price))
                print("Added " + symbol + " to portfolio.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Stock symbol not found in prices dictionary.")

    print("\n--- Portfolio Summary ---")
    for item in portfolio:
        print(item)
    print("Total Investment Value: $" + str(total_value))

    save_choice = input("\nSave result to file? (yes/no): ").lower()
    if save_choice == 'yes':
        # Fixed path for OneDrive Desktop
        desktop_path = os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Desktop', 'portfolio_summary.txt')
        
        try:
            with open(desktop_path, "w") as file:
                file.write("Stock Portfolio Summary\n")
                file.write("-----------------------\n")
                for item in portfolio:
                    file.write(item + "\n")
                file.write("-----------------------\n")
                file.write("Total Value: $" + str(total_value))
            print("Summary saved to your Desktop at: " + desktop_path)
        except FileNotFoundError:
            # Fallback if OneDrive folder structure is different
            with open("portfolio_summary.txt", "w") as file:
                file.write("Total Value: $" + str(total_value))
            print("Saved to the same folder as your script instead.")

if __name__ == "__main__":
    stock_portfolio_tracker()