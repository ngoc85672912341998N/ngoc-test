from fastapi import FastAPI


from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


from fastapi import BackgroundTasks, Depends, FastAPI
import time
app = FastAPI()

def selenium(email: str, message=""):
    BROWSERSTACK_USERNAME = "tranngocminh_AFiWRo"
    BROWSERSTACK_ACCESS_KEY = "8anY1yMSZhs7qsHCzLeD"
    URL = "https://hub.browserstack.com/wd/hub"

    bstack_options = {
        "os": "OS X",
        "osVersion": "Monterey",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack single python",
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    bstack_options["source"] = "python:sample-main:v1.0"
    options = ChromeOptions()
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)
    driver.get(email)
    link_avartar=[]
    time.sleep(5)
    value = driver.find_elements(By.TAG_NAME, 'video')
    k5=[]
    for value in value:
        print(value.get_attribute("data-src"))
        k3=value.get_attribute("data-src")
        k10=str(k3)
        k= len(k10.split("/"))
        print(k10.split("/")[k-1].split(".")[0])
        k5= str(k10.split("/")[k-1].split(".")[0])
        k4 =str(k5)+","+str(k3)+"\n"
        k5.append(k)
    driver.quit()
    return k5
@app.get("/")
async def root(email: str,background_tasks: BackgroundTasks):
    background_tasks.add_task(selenium, email, message="some notification")
    return {"message": "xin chào bạn"}


