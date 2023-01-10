import json, re
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from os import system, getcwd, chdir
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
with open('/Users/Yousefmacer/Github/data/chainlink_analysis/chainlink/config.json') as f:
    data = json.load(f)

MAIN_PATH = data["path"]
DRIVER_PATH = data["driver"]
