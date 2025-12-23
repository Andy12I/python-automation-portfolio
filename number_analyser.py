print("Enter 5 numbers:")
numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nYou entered:", numbers)
print("The smallest number is:", min(numbers))
print("The largest number is:", max(numbers))
print("The sum of the numbers is:", sum(numbers))
print("The average is:", sum(numbers) / len(numbers))
