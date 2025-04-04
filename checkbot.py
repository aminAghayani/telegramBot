import requests
from bs4 import BeautifulSoup

URL = "https://aminaghayani.github.io/studenwerk/"

# Fetch the webpage
response = requests.get(URL)
if response.status_code != 200:
    print(f"Failed to fetch the page! Status Code: {response.status_code}")
    exit(1)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find the select dropdown
select = soup.find("select", {"id": "citySelect"})
if not select:
    print("Could not find the city dropdown!")
    exit(1)

# Extract available cities
available_cities = []
for option in select.find_all("option"):
    city = option.get("value")
    is_disabled = "disabled" in option.attrs

    if city and not is_disabled:
        available_cities.append(city)

# Print available cities
if available_cities:
    print("✅ Available Cities:", ", ".join(available_cities))
else:
    print("❌ No cities available.")
