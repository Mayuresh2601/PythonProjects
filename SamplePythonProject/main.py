import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\MAYURESH\\Documents\\chromedriver.exe")

driver.maximize_window()
driver.get("https://app-test.ekincare.com/dashboard")

driver.find_element_by_xpath("//input[@type='email']").send_keys("raghunath@ekincare.com")
time.sleep(5)

driver.find_element_by_xpath("//input[@type='password']").send_keys("Ekincare@123R")
time.sleep(5)

driver.find_element_by_xpath("//input[@type='checkbox']").click()
time.sleep(5)

driver.find_element_by_xpath("//button[text()='Get Started']").click()
time.sleep(20)

print(driver.title)  # Print the name of the website

driver.close()  # Close the window