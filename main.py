import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,fr;q=0.7,es;q=0.6"
}

response = requests.get("https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E475&minBedrooms=2&maxPrice=300000&sortType=1&propertyTypes=&maxDaysSinceAdded=14&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords=")

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".propertyCard-details a")
all_links = []

for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://rightmove.co.uk{href}")
    else:
        all_links.append(href)

all_address_elements = soup.select(".propertyCard-details address")

all_addresses = [address.get_text().replace("\n", "") for address in all_address_elements]


all_price_elements = soup.select(".propertyCard-priceValue")
all_prices = [price.get_text().strip() for price in all_price_elements if "£" in price.text]

all_price_qualifier_elements = soup.select(".propertyCard-priceQualifier")
all_qualifiers = [qualifier.get_text().strip() for qualifier in all_price_qualifier_elements]

all_prices_with_qualifiers = [' '.join(combination) for combination in zip(all_qualifiers, all_prices)]
print(all_prices_with_qualifiers)