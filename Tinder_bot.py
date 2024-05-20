from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)
driver.get(url="https://tinder.com/app/recs")
time.sleep(7)
decline_cookies=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]/div")
decline_cookies.click()
time.sleep(5)
log_in=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
log_in.click()
time.sleep(7)
try:
    more_option = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/button")
    more_option.click()
    time.sleep(7)
finally:
    facebook_login = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button")
    facebook_login.click()
    time.sleep(6)
    try:
        acc_recovery=driver.find_element(By.XPATH,'//*[@id="t338671021"]/div/div/div[2]/button')
        acc_recovery.click()
        time.sleep(5)
        log_in = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
        log_in.click()
        time.sleep(5)
        facebook_login = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button")
        facebook_login.click()
        time.sleep(5)
    except:
       pass


#Switch to Facebook login window
time.sleep(7)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

EMAIL="YOUR EMAIL"
PASSWORD="YOUR TINDER PASSWORD"
time.sleep(3)
email_input=driver.find_element(By.XPATH,'//*[@id="email"]')
password_input=driver.find_element(By.XPATH,'//*[@id="pass"]')
email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)
time.sleep(3)
#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(7)
location_allow=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/button[1]')
location_allow.click()
time.sleep(7)
notification_deny=driver.find_element(By.XPATH,'//*[@id="t338671021"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]')
notification_deny.click()
time.sleep(7)
#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(30):

    #Add a 1 second delay between likes.
    time.sleep(2)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            "//*[@id='t2067052097']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")
        like_button.click()
        time.sleep(5)

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
