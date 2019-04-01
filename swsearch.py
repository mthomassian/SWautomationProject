from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

def findCheap():
    site = driver.page_source
    soup = BeautifulSoup(site,'html.parser')
    getaway = soup.find_all('span', attrs={'class': 'fare-button--value-total'})
    for prices in getaway:
        price = prices.contents[0]
        if int(price) < int(maxprice):
           cheap.append(price)

leave = input('Departing airport (3 letter code only, e.g. SJC): ')
arrive = input('Destination airport (3 letter code only, e.g.SNA): ')
depart = input('Departure Date (m/dd or mm/dd format): ')
maxprice = input('Enter a price to search below, e.g. type 70 for flights under $70: ')
cheap = []
flights = []    
driver= webdriver.Chrome()
driver.get("https://southwest.com")

oneway = driver.find_element_by_xpath('//input[@value="oneway"]').click()

search = driver.find_element_by_id('LandingPageAirSearchForm_originationAirportCode')
search.clear()
search.send_keys(leave)

search2 = driver.find_element_by_id('LandingPageAirSearchForm_destinationAirportCode')
search2.clear()
search2.send_keys(arrive)

search3 = driver.find_element_by_id('LandingPageAirSearchForm_departureDate')
search3.clear()
search3.send_keys(depart)

search = driver.find_element_by_id('LandingPageAirSearchForm_submit-button').click()

time.sleep(6) #return and replace with wait

findCheap()
#the following locates and clicks the link to the next day - southwest returns an error 
#searchLink = driver.find_element_by_xpath('//li[4]')
#searchLink.click()


if not cheap:
    print(f'There are not any flights below ${maxprice} on {depart}')
else:
    print(f'There are {len(cheap)} flights under ${maxprice} on {depart} to {arrive}:')
    for i in cheap:
        flights.append(f'${i}')
    print(', '.join(flights))

driver.close()
