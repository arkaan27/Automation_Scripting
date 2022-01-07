import selenium_Library as se
import logging

# Description of Base path
base_path = 'D://'
company_name = 'Novavax'
chrome_driver_path = 'C://Users/arkaa/Desktop/chromedriver.exe'

if __name__ == '__main__':


    # Creating Directory
    download_path = se.create_directory(base_path, company_name)

    # C
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
