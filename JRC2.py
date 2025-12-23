#the inventory manager
import csv #import the csv library
# create variable 
inventory = [
    ["Ingredient", "Quantity"],
    ["Basmati rice", "50kg"],
    ["Tomatoes", "10kg"]
]
# newline='' is a technical requirement for windows to prevent blank lines
with open("kitchen_stock.csv", "w", newline='') as file:
    my_writer = csv.writer(file)
    my_writer.writerows(inventory)

    print("CSV created")