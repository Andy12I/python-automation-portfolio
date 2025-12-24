# greeting.py
# This program asks for your name and age, then responds with a message.
# ask the user for their name
name = input("what's your name")


#ask for the users birth year

year = input("what's the year of your birth?" )

year = int(year)

#calculate the age
age = 2025 - (year)

Yearturn_100 = year+100

#print a personalised message

print (f"hello, {name}, You are {age} years old")
print (f"You will turn hundred in the year {Yearturn_100}")
if age<=18:
   print("You are young, Enjoy your learning journey😊")
elif age<=60:
    print("You are in your prime, Keep Pushing!")
else:
    print("Life long learning is impressive.👍")