# ask the user for total bill amount
bill = input("Your total bill amount is?")
# ask the user for total number of people
people = input("How many people in your group")
# calculate the individual bill amount.
amount = float(bill)/int(people)
# print the result
print("Each person has to pay ,", amount)