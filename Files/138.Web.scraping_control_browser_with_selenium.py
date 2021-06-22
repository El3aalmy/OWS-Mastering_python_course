# ---------------------------------------------------
# -- Web scraping => Control browser with selenium --
# ---------------------------------------------------
# - Control browser with selenium for automated testing
# - Download file from the internet
# - Subtitle download and add on your movies ( many modules )
# - Get quotes from websites
# - Get gold and currencies rate
# - Get news from websites
# --------------------------------------------------

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://elzero.org")

browser.find_element_by_css_selector("#search").send_keys("Front-end developer")

browser.find_element_by_css_selector(".search-submit").click()

browser.find_element_by_css_selector(".results-container .result-box:first-of-type h3 a").click()

browser.implicitly_wait(5)

views_count = browser.find_element_by_css_selector(".page-info div:last-child span:last-child")

browser.implicitly_wait(5)

print(views_count.get_attribute('innerHTML'))

browser.quit()
