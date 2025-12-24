print("Enter product prices. Type 'done' when finished. \n")
prices = []
while True:
    item = input("Enter price: ")
    if item.lower() == 'done':
        break

    prices.append(float(item))



if len(prices) == 0 :
         print("You didn't enter a price.")
else:
     print("\nYou entered:" , prices)

    
        


total = sum(prices)
average = sum(prices) / len(prices)

print(f"Total amount: ₹{total}")
print(f"Average item price: ₹{average: .2f}")

if total > 1000 :
    print("You spent quite a bit today, Take it easy!😰")
elif total > 500 :
    print("A balanced shopping trip. Nice!🙂")
else :
    print("Very economical. Good money discipline! 👍")