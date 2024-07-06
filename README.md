# QA Test Automation

This repository contains a simple Selenium test script to verify the integration between the frontend and backend services.

## Prerequisites

1. **Python**: Ensure you have Python installed on your system.
2. **Google Chrome**: Ensure you have Google Chrome installed on your system.
3. **ChromeDriver**: Download the ChromeDriver that matches your version of Google Chrome from. Make sure to add the directory containing `chromedriver` to your system's PATH.

## Setup

1. **Clone the repository**:

   ```sh
   https://github.com/rakshith2024/qa-test
   cd qa-test


2. **Install dependencies**:

    Install the required Python packages using pip:

    ```sh
    pip install selenium


3. **Start the Service**:

     Ensure that the frontend and backend services are running. The test script assumes the frontend is accessible.
     Adjust the URL in the test script according to the local url.


4. **Run the Script**:

    Run the test script using Python

    ```sh
    python test_integration.py

The script will open a browser window, navigate to the frontend URL, and verify that the message from the backend is correctly displayed.
   
     
  

    
