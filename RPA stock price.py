### Import packages ###
# For Web automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# For time
import time
import datetime

# For system
import os

# For Google services
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

### Open the Web page ###
# Record the start time of the program
start_time = time.time()
start_date = datetime.date.today()
first_day = start_date.replace(day=1)
last_month_of_year = (first_day-datetime.timedelta(days=1)).strftime("%Y")
last_month = (first_day-datetime.timedelta(days=1)).strftime("%-m")
last_full = (first_day-datetime.timedelta(days=1)).strftime("%Y%m")

# Open chrome
driver = webdriver.Chrome()

# Open TWSE web
browser = "https://www.twse.com.tw/en/trading/historical/stock-day.html"
driver.get(browser)

# Maximize wimdow
driver.maximize_window()

### Download the target file ###
# Select the designated date
Year_select = Select(driver.find_element(By.XPATH, "//select[@id='label0']"))
Year_select.select_by_value(last_month_of_year)
Month_select = Select(driver.find_element(By.XPATH,"//select[@name='mm']"))
Month_select.select_by_value(last_month)

# Enter stock code
code = "2330" #TSMC
code_input = driver.find_element(By.XPATH, "//input[@id='label1']")
code_input.send_keys(code)

# Query
Query_btn = driver.find_element(By.XPATH, "//button[@class='search']")
Query_btn.click()

# Download
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='csv']"))
)
time.sleep(1)
Download_btn = driver.find_element(By.XPATH, "//button[@class='csv']")
Download_btn.click()

# Wait for download
timeout = 300
file_name = "STOCK_DAY_"+code+"_"+last_full+".csv"
file_path = "/Users/shan/Downloads/"+ file_name  # Default path
download_time = time.time()
while not os.path.exists(file_path):
    if time.time() - download_time > timeout:
        print("Timeout")
        break
if os.path.exists(file_path):
    print("The file is successfully downloaded")
driver.quit()

### Upload the file to Google drive
# Service account key path
key_path = {KEY PATH}

# Create Google Drive service
creds = service_account.Credentials.from_service_account_file(
    key_path, scopes=['https://www.googleapis.com/auth/drive'])
service = build('drive', 'v3', credentials=creds)

# Create metadata for the file
file_metadata = {'name': file_name}

# Specify the folder ID in Google Drive where the file will be uploaded
folder_id = {FOLDER ID}
file_metadata['parents'] = [folder_id]

# Upload the file
media = MediaFileUpload(file_path)
file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
print('File successfully uploaded to Google Drive. File ID: {}'.format(file.get('id')))

# Record the end time of the program
end_time = time.time()

# Calculate the total time taken
elapsed_time = end_time - start_time

# Convert the seconds to hours:minutes:seconds format
formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

# Remove downloaded file
os.remove(file_path)

print(f"The total time taken for program execution is: {formatted_time}")