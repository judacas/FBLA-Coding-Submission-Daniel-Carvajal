from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

query = ""
for i in range(len(sys.argv)-1):
    query = query + str(sys.argv[i+1]) + "%20"

opt = Options()
opt.add_argument("--disable-notifications")
opt.add_argument("headless")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.geolocation": 1, 
  })

browser = webdriver.Chrome(options=opt)
# browser = webdriver.Chrome()
# query = "hotels near me"
url = "https://www.tripadvisor.com/Search?q=" + query + "&blockRedirect=true"
# print("searching for attractions...")
browser.get(url)

# alert = wait.until(expected_conditions.alert_is_present())

# print("still searching for attractions...")
time.sleep(2)
# print("almost done...")

# try:
#     elements = browser.find_elements("result-title")
# except BaseException:
#     print("bruh")
#     pass
results = ""
try:
    browser.find_element(By.CLASS_NAME, "original-query").click()
    # print("aight we back to the oq!!!")
    time.sleep(1)
    # browser.find_element(By.XPATH("//*[contains(text(),'Show more')]"));
except BaseException:
    pass

try:
    browser.find_element(By.CLASS_NAME, "result-section-footer-columns").click()
except BaseException:
    # print("not found via result-section-footer-columns")
    try:
        browser.find_element(By.CLASS_NAME, "show-block").click()
    except BaseException:
        # print("not found via show-block")
        # print("not found at all")
        pass
    pass

try:
    elements = browser.find_elements(By.CLASS_NAME, "result-title")
    i = 0
    for element in elements:
        i+= 1
        try:
            span = element.find_element(By.TAG_NAME, "span")
            if(span.text != ""):
                print(span.text)
                results += span.text + "\n"
        except BaseException:
            pass
    # finalResults = open("finalResults.txt", "w")
    # finalResults.write(results + ";")
    # time.sleep(10)
    # browser.close()   
except BaseException:
    print("Sorry, couldn't find any results that matched your request\n please try again with different attributes")
    finalResults = open("finalResults.txt", "w")
    finalResults.write("Sorry, couldn't find any results that matched your request\n please try again with different attributes" + ";")
    pass
        