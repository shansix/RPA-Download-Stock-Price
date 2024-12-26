# RPA | Automating Stock Data Download and Google Drive Upload

## Overview

This script automates the process of downloading stock trading data from the Taiwan Stock Exchange (TWSE) website and uploading it to a designated Google Drive folder. It utilizes Selenium for web automation and the Google Drive API for file uploads.

## Features

1. Automated File Download:

- Accesses the TWSE website.
- Selects a specific stock by code (default: TSMC, stock code 2330).
- Downloads historical stock data for the last month.

2. File Upload to Google Drive:

- Uploads the downloaded file to a specified folder in Google Drive using a service account.

3. Execution Time Measurement:

- Records the total execution time for performance monitoring.

4. Temporary File Cleanup:

- Deletes the downloaded file after uploading it to Google Drive.

## Environment

- python 3.12.0
- selenium 4.19.0
- google-api-python-client 2.125.0
- google-auth 2.29.0
- google-auth-httplib2 0.2.0
- google-auth-oauthlib 1.2.0
