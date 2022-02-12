from importlib.resources import path
from unittest import result
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
# opt.add_argument("headless")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.geolocation": 1, 
})
browser = None
try:
    browser = webdriver.Chrome(executable_path= '.\dist\TripAdvisorSearcher\selenium\webdriver\chromedriver99.exe', options=opt)
except:
    try:
        browser = webdriver.Chrome(executable_path= '.\dist\TripAdvisorSearcher\selenium\webdriver\chromedriver98.exe', options=opt)
    except:
        try:
            browser = webdriver.Chrome(executable_path= '.\dist\TripAdvisorSearcher\selenium\webdriver\chromedriver97.exe', options=opt)
        except:
            try:
                browser = webdriver.Chrome(executable_path= '.\dist\TripAdvisorSearcher\selenium\webdriver\chromedriver87.exe', options=opt)
            except:
                results = "there was an error in starting chrom to search Trip advisor\nPlease try installing chrome version 99 and try again"
url = "https://www.tripadvisor.com/Search?q=" + query + "&blockRedirect=true"
browser.get(url)
time.sleep(2)
results = ""
try:
    browser.find_element(By.CLASS_NAME, "original-query").click()
    time.sleep(1)
except BaseException:
    pass

try:
    browser.find_element(By.CLASS_NAME, "result-section-footer-columns").click()
except BaseException:
    try:
        browser.find_element(By.CLASS_NAME, "show-block").click()
    except BaseException:
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
    # browser.close()   
except BaseException:
    print("Sorry, couldn't find any results that matched your request\n please try again with different attributes")
    finalResults = open("finalResults.txt", "w")
    finalResults.write("Sorry, couldn't find any results that matched your request\n please try again with different attributes" + ";")
    pass

finalResults = open("finalResults.txt", "w")
finalResults.write(results)
        