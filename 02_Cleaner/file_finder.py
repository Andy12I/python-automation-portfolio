import os

# The exact name you used in your script
filename = "my_scrapped_quotes.csv"

if os.path.exists(filename):
    print(f"✅ FOUND IT! The file exists at: {os.path.abspath(filename)}")
    print(f"Size: {os.path.getsize(filename)} bytes")
else:
    print("❌ NOT FOUND. Okay, now we have a real mystery.")