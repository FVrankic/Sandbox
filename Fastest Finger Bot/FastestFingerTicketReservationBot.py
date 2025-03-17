from selenium import webdriver
from selenium.webdriver.firefox.options import Options  # Import Options for Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Target time: 10:00:00 on 2025-01-18
target_time = datetime.strptime('2025-01-18 10:00:01', '%Y-%m-%d %H:%M:%S') #dodaj sekund poslje il pola sekunde poslje jer moze failat u 1000000

# Test time for demonstration (You can change this to your desired target time)
# target_time = datetime.strptime('2025-01-16 16:15:30', '%Y-%m-%d %H:%M:%S')


# Set up Firefox options to enable incognito mode
firefox_options = Options()
firefox_options.add_argument("--private")  # Enable private mode

# Path to the Firefox geckodriver executable
driver = webdriver.Firefox(options=firefox_options)  # Pass options to the driver

# # Path to the Firefox geckodriver executable
# driver = webdriver.Firefox()  # Ensure the correct path to geckodriver is set

# Open the website
# driver.get("http://localhost:8000/webpage2.html")
# driver.get("http://localhost:8000/webpage3.html")
driver.get("https://www.lfccro.com/prijave-za-utakmicu-proljece-2025/")


# Wait until the target time
while datetime.now() < target_time:
    # Continuously check the time until it matches the target time
    time.sleep(0.01)  # Sleep briefly to avoid overwhelming the CPU

# Get the current time and start measuring elapsed time
start_time = time.time()

driver.refresh()
print(f"Page refreshed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, Time elapse started!")

# Wait for the dropdown to be present
try:
    wait = WebDriverWait(driver, 10)
    dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='MatchId']")))

    # Log time elapsed when dropdown is located
    elapsed_time = time.time() - start_time
    print(f"Dropdown located, Time elapsed: {elapsed_time:.3f} seconds")

    # Select the dropdown option
    options = dropdown.find_elements(By.TAG_NAME, "option")
    selected = False

    for option in options:
        option_text = option.text

        # Check if "Everton" or "02.04." is in the option text
        if "Everton" in option_text or "02.04." in option_text:
            # Scroll into view and click
            driver.execute_script("arguments[0].scrollIntoView(true);", option)
            driver.execute_script("arguments[0].selected = true;", option)
            driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", dropdown)
            selected = True
            print(f"Selected option: {option.text}, Time elapsed: {elapsed_time:.3f} seconds")
            break

    # If no option containing "Everton" or "02.04." is found, select the second option
    if not selected and len(options) > 1:
        second_option = options[1]
        driver.execute_script("arguments[0].scrollIntoView(true);", second_option)
        driver.execute_script("arguments[0].selected = true;", second_option)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", dropdown)
        print(f"Fallback: Selected second option: {second_option.text}, Time elapsed: {elapsed_time:.3f} seconds")


    # Wait for the submit button to become clickable
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button button-primary match-application']")))

    # Log time elapsed after locating the submit button
    elapsed_time = time.time() - start_time
    print(f"Submit button located, Time elapsed: {elapsed_time:.3f} seconds")

    # Adding aditional waiting time
    # Wait in a loop until 3.5 seconds have passed
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 2.5:
            break  # Exit the loop when 2.5 seconds have passed
        time.sleep(0.1)  # Add a short sleep to avoid maxing out the CPU

    # Submit the form
    submit_button.click()

    # Log time elapsed after form submission
    elapsed_time = time.time() - start_time
    print(f"Form submitted, Time elapsed: {elapsed_time:.3f} seconds")

except Exception as e:
    print(f"Error: {e}")

# Finally, wait for a few seconds to observe the outcome
time.sleep(10)

# Quit the driver after a small delay
driver.quit()

# Log time elapsed when driver quits
elapsed_time = time.time() - start_time
print(f"Driver quit, Time elapsed: {elapsed_time:.3f} seconds")
