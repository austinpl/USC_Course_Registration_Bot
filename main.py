import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options to speed up Selenium
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run in headless mode
# options.add_argument('--disable-gpu')  # Disable GPU
# options.add_argument('--no-sandbox')  # Bypass OS security model
# options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
# options.add_argument('--blink-settings=imagesEnabled=false')  # Disable images
# options.add_argument('--disable-extensions')  # Disable extensions
# options.add_argument('--disable-infobars')  # Disable infobars
# options.add_argument('--start-maximized')  # Start maximized

# Boolean to check if registration successful, exit program if so
success = False

while not success:

    # Initialize the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Create login boolean to check if login successful, reset if not
    login = False

    # Login info (insert your own here)
    username = 'austinpl'
    password = 'Gamer04052004!!!'

    # LOGIN LOOP (KEEP LOOPING UNTIL SUCCESS)
    while not login:
        # Launch chromedriver (include in loop so reset if errors)
        url = 'https://my.usc.edu'
        driver.get(url)
        try:
            # Wait until login button shows up
            user_wait = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "netid"))
            )
            print('User form found.')
            username_field = driver.find_element(By.ID, "netid")
            password_field = driver.find_element(By.ID, "password")
            username_field.send_keys(username)
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)

            # Wait a minute for duo mobile approval
            duo_wait = WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.ID, "trust-browser-button"))
            ).click()
            print('Duo button found.')

            # Check if approve device window shows up. If so, click button, if not reset.
            webreg_wait = WebDriverWait(driver, 120).until(
                    EC.element_to_be_clickable((By.ID, "services-1030"))
            ).click()
            print('Web Registration button found.')
            login = True
        except Exception as e:
            print('An error has occurred.')
            driver.quit()
            time.sleep(5)
            break
    try:
        # SWITCHING TABS TO REGISTRATION PAGE
        current_window = driver.current_window_handle

        # Get all window handles after the new tab is opened
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        new_window = [window for window in driver.window_handles if window != current_window][0]

        # Switch to the new tab
        driver.switch_to.window(new_window)
        print("Switched to the new tab.")

        # Select the term (Fall 2024)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "termLink1"))
        ).click()
        print('Term button found.')

        # Click on checkout button
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "mItReg"))
        ).click()
        print('Checkout button found.')

        while not success:
            try:
                try:
                    # Check if registration is unavailable
                    registration_unavailable_element = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        "/html/body/div/div[2]/div/div[1]/div/div/div/h5"))
                    )
                    if registration_unavailable_element.text == 'You cannot register for following reason(s):':
                        print("Registration unavailable, refreshing the page.")
                        driver.refresh()
                        continue  # Skip the rest of the loop and start over
                except:
                    # If the element is not found, continue with the registration check
                    pass
                registration_status_element = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "/html/body/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div/div/span[5]/span[2]"))
                )
                registration_status = registration_status_element.text
                print(f"Registration status: {registration_status}")

                if registration_status == 'Closed':
                    print("Registration is closed, refreshing the page.")
                    driver.refresh()
                else:
                    driver.find_element(By.ID, "SubmitButton").click()
                    WebDriverWait(driver, 60).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/span[1]"))
                    )
                    checkout_message_element = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/span[1]")
                    checkout_message = checkout_message_element.text
                    print(f"Checkout Message: {checkout_message}")
                    if 'successful' in checkout_message.lower():
                        success = True
                        print("Registration successful.")
            except Exception as e:
                print(f"Error during registration status check: {e}")
                break
    except Exception as e:
        print(f"Error during registration process: {e}")
    finally:
        driver.quit() # Ensure the driver is closed after each attempt
        if not success:
            time.sleep(5) # Wait before retrying if registration was not successful