# USC Course Registration Bot
The University Course Registration Bot is a Python-based automation tool designed to streamline and automate the course registration process for students at USC. This bot interacts with the university's course registration website to help students enroll in classes efficiently, reducing the hassle and stress associated with manual registration.

## Challenges of Manual Course Registration
For students at USC, and university students in general, registering for classes can be a daunting and stressful task. The competition for a limited number of open spots during course registration day often leads to frustration and disappointment. High network traffic can cause significant delays, making it difficult to secure your desired classes. Additionally, the constant need to monitor the course registration website for openings or waitlist updates adds to the stress. These issues highlight the need for a more efficient and streamlined registration process.

## The Solution
To address the challenges of manual course registration, this project offers an automated solution that leverages web automation technology. The Course Registration Bot is designed to handle the entire registration process from login to course selection, minimizing the need for manual intervention and ensuring that students have the best chance of enrolling in their desired classes.

### How the Bot Works
The bot automates the registration process using Selenium, a powerful web automation tool. Here's an overview of how it functions:

#### Setup and Initialization:
* The bot uses the webdriver-manager library to automatically manage ChromeDriver installation and updates, ensuring compatibility with the latest browser versions.
* Several Chrome options are configured to optimize performance, such as running in headless mode and disabling unnecessary features like images and extensions.
#### Login Automation:
* The bot opens the university's login page and waits for the login form to appear.
* It enters the user's credentials (username and password) and submits the form.
* Two-factor authentication (2FA) is handled *partially* by waiting for users to approve the Duo Mobile prompt.
#### Navigating to Registration:
* Once logged in, the bot navigates to the course registration page by switching to the appropriate browser tab.
* It selects the desired term (e.g., Fall 2024) and prepares for the registration process.
#### Automated Registration:
* The bot continuously checks the registration status, looking for open slots in the desired courses.
* If registration is unavailable or closed, the bot refreshes the page and tries again.
* Upon finding an open slot, the bot submits the registration request.
#### Success Confirmation:
* The bot monitors the registration process for success messages.
* If registration is successful, the bot prints a confirmation message and exits.
* If not, it retries after a short delay, ensuring persistence in securing a spot.
#### Error Handling:
* The bot includes comprehensive error handling to manage unexpected issues, such as network failures or incorrect login details.
* It gracefully exits and retries as needed, ensuring reliability and robustness.

## Integration with Cloud Computing (AWS EC2)
While the course registration bot is designed to automate the registration process effectively, running it on a local PC can be inefficient and problematic for several reasons:
* A local PC cannot reliably run 24/7 without interruptions due to power outages, system updates, or hardware failures.
* Local machines may struggle with resource-intensive tasks, leading to slower performance and increased latency during peak registration times.
* Home networks are often less stable and secure than cloud-based networks, leading to potential connectivity issues.
