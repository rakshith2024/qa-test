from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Replace with the path to your ChromeDriver
CHROMEDRIVER_PATH = "C:\\chromedriver.exe"
URL = "http://127.0.0.1:50881/"  # Replace with the actual URL


def test_integration():
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get(URL)

    time.sleep(10)

    message_element = driver.find_element(By.XPATH, '//h1')  # Replace 'message' with the actual id

    assert message_element.text == "Hello from the Backend!", f"Expected 'Hello from the Backend!' but got '{message_element.text}'"

    driver.quit()


if __name__ == "__main__":
    test_integration()