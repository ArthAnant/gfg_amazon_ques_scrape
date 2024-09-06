from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/amazon-sde-sheet-interview-questions-and-answers/")
list_of_names = []

rows = driver.find_elements("xpath", "//table//tbody//tr")

scroll_pos = 2700
for element in range(len(rows)):
    row = driver.find_element("xpath", f"//table//tbody//tr[{element+1}]")
    driver.execute_script("window.scrollTo(0, 1600)")
    time.sleep(2)
    read_more = driver.find_element("xpath", "//div[@class='read-more-container']").click()
    time.sleep(3)
    driver.execute_script(f"window.scrollTo(0, {scroll_pos})")
    time.sleep(1)
    solve_button = row.find_element("xpath", f"//table//tbody//tr[{element+1}]//td[2]//a").click()
    time.sleep(3)
    title_to_append = driver.find_element("xpath", "//h3[@class='g-m-0']").text
    list_of_names.append(title_to_append)
    driver.back()
    driver.execute_script("window.scrollTo(0, 0)")
    scroll_pos += 80
    print(list_of_names)



driver.quit