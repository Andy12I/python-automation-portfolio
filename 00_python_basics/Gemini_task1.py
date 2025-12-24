# 'w' means Write mode. It creates 'test.txt' if it doesn't exist.
with open("test.txt", "w") as file:
    file.write("This is line 1.\n") # \n is the 'New Line' character (Enter key)
    file.write("This is line 2.\n")

print("File created successfully!")

# 'r' means Read mode.
with open("test.txt", "r") as file:
    content = file.read() # Reads the ENTIRE file into a string variable

print("Here is what was in the file:")
print(content)

with open("test.txt", "a") as file:
    file.write("This is a NEW line added later.\n")