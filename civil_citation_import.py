
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load Excel data
excel_file = "path/to/civil_citations.xlsx"
data = pd.read_excel(excel_file)

# Format date columns
if "CitDate" in data.columns:
    data["CitDate"] = pd.to_datetime(data["CitDate"], errors="coerce").dt.strftime("%Y-%m-%d")

data = data.fillna("")

# Set up Selenium WebDriver
chrome_driver_path = "path/to/chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Log in to OpenGov
driver.get("https://your-opengov-login-url.com")  # Replace with actual URL

WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='email-test']"))
)

# Login (enter dummy credentials for public repo)
driver.find_element(By.XPATH, "//input[@id='email-test']").send_keys("your.email@example.com")
driver.find_element(By.ID, "password-test").send_keys("your_password_here")
driver.find_element(By.CLASS_NAME, "auth0-label-submit").click()

time.sleep(5)  # Wait for login to complete

# Process each record
for index, row in data.iterrows():
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-test='create_new_action_button_Create Record']"))
    )
    driver.find_element(By.XPATH, "//button[@data-test='create_new_action_button_Create Record']").click()

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[h5[text()='Legacy Civil Citations']]"))
    )
    driver.find_element(By.XPATH, "//a[h5[text()='Legacy Civil Citations']]").click()
    time.sleep(2)

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "customInput_21726"))
    )

    driver.find_element(By.ID, "customInput_21726").send_keys(str(row["CitDate"]))
    driver.find_element(By.ID, "customInput_21727").send_keys(str(row["No."]))
    driver.find_element(By.ID, "customInput_21728").send_keys(row["Location"])
    # ... continue for all fields ...

    driver.find_element(By.ID, "submit-record").click()

    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element((By.ID, "submit-record"))
    )
    WebDriverWait(driver, 30).until(
        EC.url_changes(driver.current_url)
    )

driver.quit()
