from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Set up Chrome WebDriver (Headless mode)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in the background without opening the browser
driver = webdriver.Chrome(options=chrome_options)

# Open the webpage
driver.get("https://aminaghayani.github.io/studenwerk/")

# Find the option you want to enable (Dortmund in this case)
option = driver.find_element(By.ID, "opt-dortmund")

# Remove the "disabled" attribute to enable it using JavaScript
driver.execute_script("arguments[0].removeAttribute('disabled')", option)

# Wait for the JavaScript changes to be applied
time.sleep(2)

# Get the updated page HTML after JS modifications
updated_html = driver.page_source

# Now parse the updated HTML with BeautifulSoup
soup = BeautifulSoup(updated_html, "html.parser")

# Extract available cities from the updated HTML
available_cities = []
select = soup.find("select", {"id": "citySelect"})
if select:
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

# Close the browser window
driver.quit()
