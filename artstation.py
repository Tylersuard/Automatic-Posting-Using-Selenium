
import time
from datetime import date, timedelta
import datetime

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains

url = 'https://www.artstation.com/'

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
print("driver loaded, getting url")
driver.get(url)
print("url gotted")
time.sleep(1)

sign_in = driver.find_element_by_css_selector('span.bs-btn > span:nth-child(2)').click()
print("signing in")
time.sleep(5)

username = driver.find_element_by_id("user_email")
username.clear()
username.send_keys("myname@email.com")

time.sleep(1)

password = driver.find_element_by_name("password")
password.clear()
password.send_keys("P@$$w0rd")

time.sleep(1)

sign_in_submit_form = driver.find_element_by_css_selector('div.bs-form-group:nth-child(4) > button:nth-child(1)').click()

time.sleep(30)

print("signed in")
today = datetime.date.today()

art_upload_page = driver.get('https://www.artstation.com/community/projects/new')

print("at art page")
time.sleep(20)

print(driver.current_url)

#name all the things

collection_title = driver.find_element_by_xpath("/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[1]/div[1]/fieldset/form-input/div/input")
collection_title.send_keys("Images Created By Artificial Intelligence " + str(today))

time.sleep(10)

print("titled")

description = driver.find_element_by_xpath("/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[1]/div[2]/fieldset/form-text/div/textarea")
print(description)
description.send_keys("Images created using artificial intelligence.")

print("described")
time.sleep(10)

medium_category = driver.find_element_by_css_selector('div.medium:nth-child(1) > label:nth-child(1) > span:nth-child(3)').click()

print("medium set")
time.sleep(5)

subject_matter = driver.find_element_by_css_selector("#category-input-field")
subject_matter.send_keys("abstract")
subject_matter = driver.find_element_by_xpath("/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[1]/div[3]/fieldset/project-categories/div/div/div[1]/div[1]/perfect-scrollbar/div/div[1]/div[1]/span/button").click()
print("subject matter set")
time.sleep(5)

tags = driver.find_element_by_css_selector(".select2-search__field")
tags.send_keys("artificial intelligence")
tags.send_keys(Keys.RETURN)

print("tagged")
time.sleep(5)

#upload the shit
launch_day = datetime.date(2020, 8, 28)
diff = today - launch_day
day_iterator = int(diff.days)
image_batch_iterator = "batch" + str(day_iterator)
art_folder = "/root/ai_art_images/"

# uncomment this later after testing
for i in range(0,7):
    k = 6 - i
    time.sleep(15)
    try:
        art_path = art_folder + image_batch_iterator + "step" + str(k) + ".png"
        upload_image = driver.find_element_by_xpath("/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[1]/project-assets-uploader/div[1]/span/input").send_keys(art_path)
    except:
        print("no file with that name")
#delete after testing

print("images uploaded")

time.sleep(30) #change to 120 later
#submit that shit

submit = driver.find_element_by_xpath("/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[2]/div[2]/fieldset/button[2]")

actions = ActionChains(driver)
actions.move_to_element(submit).click().perform()

print("image saved")
driver.close()
