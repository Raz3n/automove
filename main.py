import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,fr;q=0.7,es;q=0.6"
}