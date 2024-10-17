from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options (optional)
options = Options()

# Specify the path to ChromeDriver
service = Service(r"C:\Users\Ayush\OneDrive\Desktop\Downloads\chromedriver-win64\chromedriver.exe")  # Update this path if necessary

# Create a WebDriver instance
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Open the Amazon India webpage
driver.get('https://www.amazon.in')

# Step 2: Wait for the page to load and verify the title
try:
    WebDriverWait(driver, 10).until(EC.title_contains("Amazon.in"))
    print(f"Page Title: {driver.title}")

    # Step 3: Check if the title matches the expected title
    if "Amazon.in" in driver.title:
        print("Test Passed: Title matches.")
    else:
        print("Test Failed: Title does not match.")

    # Step 4: Locate the search box
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))

    print("Search box found!")

    # Step 5: Type a query into the search box
    search_box.send_keys("laptop")

    # Step 6: Submit the search form
    search_box.submit()

    # Wait for the results to load
    WebDriverWait(driver, 10).until(EC.url_contains("laptop"))

    # Step 7: Print the current URL
    print(f"Current URL after search: {driver.current_url}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Step 8: Close the browser
    driver.quit()
