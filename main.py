# github.com/seyhanvankhan/nhs-vaccine

# WARNING: Only use this program if these 2 questions are "No"
# - Have you had the flu vaccine in the past 7 days?
# - Do you have a flu vaccine appointment soon?

first_name = ""
surname = ""
postcode = ""

birthdate_day = ""
birthdate_month = ""
birthdate_year = ""

furthest_acceptable_place_in_miles = 5.0

# have a look at example-of-personal-details.png if stuck!







################################################################################

from os import system
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if not(first_name and surname and postcode and birthdate_day and birthdate_month and birthdate_year):
  print("\nOpen main.py and fill in your details.\nHave a look at example-of-personal-details.png if stuck!\n")
  exit()

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.nhs.uk/book-a-coronavirus-vaccination/do-you-have-an-nhs-number")

# Do you know your NHS number?
driver.find_element_by_id("option_No_input").click()
driver.find_element_by_id("submit-button").click()

# What is your name?
driver.find_element_by_id("Firstname").send_keys(first_name)
driver.find_element_by_id("Surname").send_keys(surname)
driver.find_element_by_id("submit-button").click()

# What is your date of birth?
driver.find_element_by_id("Date_Day").send_keys(birthdate_day)
driver.find_element_by_id("Date_Month").send_keys(birthdate_month)
driver.find_element_by_id("Date_Year").send_keys(birthdate_year)
driver.find_element_by_id("submit-button").click()

# What is your postcode?
driver.find_element_by_id("Postcode").send_keys(postcode)
driver.find_element_by_id("submit-button").click()

# You may need to book your vaccination appointment
driver.find_element_by_id("submit-button").click()

# Have you had the flu vaccine in the past 7 days?
driver.find_element_by_id("option_No_input").click()
driver.find_element_by_id("submit-button").click()

# Do you have a flu vaccine appointment soon?
driver.find_element_by_id("option_No_input").click()
driver.find_element_by_id("submit-button").click()

# Find a vaccination centre - Enter a postcode
driver.find_element_by_id("StepControls_0__Model_Value").send_keys(postcode)
driver.find_element_by_class_name("next-button").click()

# Do you have any access needs?
driver.find_element_by_class_name("next-button").click()

while True:
  distanceHTML = driver.find_element_by_class_name("distance").get_attribute('innerHTML')
  distance = float(distanceHTML[:distanceHTML.index(' ')])
  if distance < maximum_distance:
    nameElement = driver.find_element_by_class_name("SiteSelector")
    name = nameElement.get_attribute('innerHTML')
    # Announce vaccine site with text-to-speech
    system(f'say "{name}. {distance} miles"')
    nameElement.click()
    break

  sleep(3)
  driver.execute_script("location.reload(true);")
