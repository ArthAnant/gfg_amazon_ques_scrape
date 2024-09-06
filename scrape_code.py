from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/amazon-sde-sheet-interview-questions-and-answers/")
list_of_names = []
time.sleep(2)
driver.execute_script("window.scrollTo(0, 1600)")
time.sleep(2)
read_more = driver.find_element("xpath", "//div[@class='read-more-container']").click()
time.sleep(3)

rows = driver.find_elements("xpath","//table/tr")

for element in range(len(rows)):
    driver.execute_script("window.scrollTo(0, 2700)")
    time.sleep(1)
    solve_button = element.find_element("xpath", "//table//tbody//tr//td[2]//a").click()
    time.sleep(3)
    title_to_append = element.find_element("xpath", "//h3[@class='g-m-0']").text
    list_of_names.append(title_to_append)
    driver.back()
    print(list_of_names)



driver.quit