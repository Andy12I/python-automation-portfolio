import requests
from bs4 import BeautifulSoup

# 1. Define the URL we want to visit
url = "https://example.com"

# 2. Ask the 'driver' to fetch the page
page = requests.get(url)

# 3. Check if it worked (200 means OK, 404 means Not Found)
print(f"Status Code: {page.status_code}")

# 4. Create the Soup (The parsed HTML)
soup = BeautifulSoup(page.text, "html.parser")

# 5. Extract specific data
# We want the text inside the <h1> tag (The main header)
header_text = soup.h1.text

print(f"The header of the site is: {header_text}")