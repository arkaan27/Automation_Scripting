"""
This is Selenium Library used to automate Downloads from link

Author: Arkaan Quanunga,

Date: 07/01/2022

"""
# Imports
import os
import logging
from selenium import webdriver

# Basic Logging
logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s'
)


def create_directory(base_path, company_name):
    """
    Creates a directory for the company name in base_path

    :param base_path: base directory of the download (str)
    :param company_name: Company name (str)
    :return: download_path
    """

    # Checking to see if base_path and company_name are strings
    try:
        logging.info("base_path = {} \n company_name= {}".format(base_path, company_name))
        assert isinstance(base_path, str)
        assert isinstance(company_name, str)
        download_path = os.path.join(base_path, company_name)
        # Create Directory if does not exist
        if not os.path.exists(download_path):
            os.mkdir(download_path)
            logging.info("SUCCESS: Created the directory")
            print("Directory ", download_path, " Created ")
        else:
            logging.error("ERROR: This directory already exists")
            print("Directory ", download_path, " already exists")
        return download_path
    except (TypeError, AssertionError):
        logging.error("ERROR: The base path/ company name is not a string")


def start_driver(download_path, chrome_driver_path):
    """
    Starts the driver

    :param download_path: download directory path (str)
    :param chrome_driver_path: chrome driver path (str)
    :return: driver
    """
    # Starts the Driver
    try:

        # Logs the info
        logging.info("download_path = {} \n chrome_driver_path = {}".format(download_path, chrome_driver_path))

        # Checks the Arguments are strings
        assert isinstance(download_path, str)
        assert isinstance(chrome_driver_path, str)

        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)
        logging.info('SUCCESS: Webdriver successfully started')
        return driver
    except AssertionError:
        logging.error('ERROR: download_path or chrome_driver_path must a str')



def open_link(driver, link):
    """

    :param driver: driver of Selenium described through function start_driver (WebElement)
    :param link: Website to be automated (str)
    :return:
    """
    # Opens the link
    driver.get(link)
    driver.maximize_window()

# def company_search(company_name, time_frame):
#
#
