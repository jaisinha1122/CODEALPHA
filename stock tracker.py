# Stock prices
stocks = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 150,
    "AMAZON": 200
}

total = 0

print("STOCK PORTFOLIO TRACKER")

stock_name = input("Enter stock name: ")
quantity = int(input("Enter quantity: "))

if stock_name in stocks:

    total = stocks[stock_name] * quantity

    print("Stock Price:", stocks[stock_name])
    print("Total Investment:", total)

    file = open("portfolio.txt", "w")

    file.write("Stock: " + stock_name + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Investment: " + str(total))

    file.close()

    print("Result saved in portfolio.txt")

else:
    print("Stock not found")