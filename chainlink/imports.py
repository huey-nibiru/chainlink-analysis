import json, re
import requests
from os import system, getcwd, chdir
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


 # Opening JSON file
with open('/Users/Yousefmacer/Github/data_analytics/chainlink_analysis/chainlink/config.json') as f:
    data = json.load(f)

MAIN_PATH = data["path"]
DRIVER_PATH = data["driver"]
