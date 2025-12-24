print("Enter product prices. Type 'done' when finished.\n")
prices = []

while True:
    item = input("Enter price: ")
    if item.lower() == "done":
        break
    prices.append(float(item))

if len(prices) == 0:
    print("No prices entered. Exiting.")
    exit()

# Save to file
with open("prices.csv", "w") as file:
    for price in prices:
        file.write(str(price) + "\n")

print("\nPrices saved to prices.csv ✅")

total = sum(prices)
average = total / len(prices)

print(f"Total: ₹{total}")
print(f"Average price: ₹{average:.2f}")
