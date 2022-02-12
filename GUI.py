from tkinter import *
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys


# Function for closing the window or exiting the app
def closeApp():
    windowApp.destroy()

#Function for searching trip advisor for results 
def search():
    query = attraction.get() + " in " + city.get()+", "+state.get()
    queryLabel.config(text= "Looking for " + query)
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
                    browser.close()
                    results = "there was an error in starting chrom to search Trip advisor\nPlease try installing chrome version 99 and try again"
                    resultLabel.config(text= results)
                    return
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
        browser.close()   
    except BaseException:
        browser.close()
        results = "Sorry, couldn't find any results that matched your request\n please try again with different attributes"
        resultLabel.config(text= results)
            



windowApp = Tk()
windowApp.title("Attractions Finder")
windowApp.geometry('500x500')

instructions1 = "Please enter the type of attraction you want to"
instructions2 = "search for (i.e. hotel, restaurant, public park"

instructions1Label = Label(windowApp, text=instructions1, fg='blue')
instructions1Label.grid(row=15,column=0,padx=5,pady=1)
instructions2Label = Label(windowApp, text=instructions2, fg='blue')
instructions2Label.grid(row=16,column=0,padx=5,pady=1)

attraction=StringVar()
attractionSearch = "Attractions"
attractionLabel = Label(windowApp, text=attractionSearch, fg='blue')
attractionLabel.grid(row=20,column=0,padx=5,pady=1)
attractionTextBox=Entry(windowApp,textvariable=attraction,fg='blue')
attractionTextBox.grid(row=21,column=0)

city=StringVar()
citySearch = "City"
cityLabel = Label(windowApp, text=citySearch, fg='blue')
cityLabel.grid(row=23,column=0,padx=5,pady=1)
cityTextBox=Entry(windowApp,textvariable=city,fg='blue')
cityTextBox.grid(row=24,column=0)

state=StringVar()
stateSearch = "State"
stateLabel = Label(windowApp, text=stateSearch, fg='blue')
stateLabel.grid(row=26,column=0,padx=5,pady=1)
stateTextBox=Entry(windowApp,textvariable=state,fg='blue')
stateTextBox.grid(row=27,column=0, pady = 25)

# Button to submit the search
searchButton = Button(windowApp, command=search, text="Search")
searchButton.grid(row=28,column=0)

queryLabel=Label(windowApp, fg='green')
queryLabel.grid(row=30,column=0,sticky=W,pady=0)

resultLabel=Label(windowApp, fg='green')
resultLabel.grid(row=30,column=1,sticky=W,pady=0)

# Button for exiting the application
exitButton = Button(windowApp, text="Exit App",command=closeApp)
exitButton.grid(row=38,column=0,pady=20)


windowApp.mainloop()
