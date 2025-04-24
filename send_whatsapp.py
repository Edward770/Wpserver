from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def send_messages(number, filepath, delay):
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=./user_data")
    driver = webdriver.Chrome(options=options)

    driver.get("https://web.whatsapp.com")
    input("Press Enter after scanning QR code...")

    with open(filepath, "r", encoding="utf-8") as file:
        messages = file.readlines()

    driver.get(f"https://wa.me/{number}")
    time.sleep(5)

    try:
        driver.find_element(By.XPATH, '//a[contains(@href, "web.whatsapp.com/send")]').click()
        time.sleep(8)
    except:
        print("Error clicking 'Continue to Chat'")
        driver.quit()
        return

    for msg in messages:
        msg = msg.strip()
        if msg:
            msg_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
            msg_box.send_keys(msg + Keys.ENTER)
            time.sleep(delay)

    driver.quit()
