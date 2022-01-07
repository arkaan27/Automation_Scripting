import selenium_Library as se
import logging

# Description of Base path
base_path = 'D://'
company_name = 'Novavax'
chrome_driver_path = 'C://Users/arkaa/Desktop/chromedriver.exe'
link = 'https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=3&ssid=14&smid=8'

if __name__ == '__main__':


    # Creating Directory
    download_path = se.create_directory(base_path, company_name)

    # Starts the driver
    driver = se.start_driver(download_path, 1)

    # Opens link
    #se.open_link(driver, link)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
