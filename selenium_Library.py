"""
This is Selenium Library used to automate Downloads from link

Author: Arkaan Quanunga,

Date: 07/01/2022

"""
# Imports
import os
import logging
from selenium import webdriver
import time

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
        logging.info(
            "base_path = {} \n company_name= {}".format(
                base_path, company_name))
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
        logging.info(
            "download_path = {} \n chrome_driver_path = {}".format(
                download_path, chrome_driver_path))

        # Checks the Arguments are strings
        assert isinstance(download_path, str)
        assert isinstance(chrome_driver_path, str)

        # Changes the driver Download path
        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        # Starts th Driver
        driver = webdriver.Chrome(
            chrome_driver_path,
            chrome_options=chrome_options)

        # Logs the info
        logging.info('SUCCESS: Webdriver successfully started')
        return driver
    except AssertionError:
        logging.error('ERROR: download_path or chrome_driver_path must a str')
        print('The driver did not start, please check log file')


def open_link(driver, link):
    """

    :param driver: driver of Selenium described through function start_driver (WebElement)
    :param link: Website to be automated (str)
    :return:
    """
    # Opens the link
    try:
        # Storing input variable in results file
        logging.info("\n Link = {}".format(link))

        # Making sure that link is a string and driver is not none
        assert isinstance(link, str)
        assert driver is not None
        driver.get(link)
        driver.maximize_window()
        logging.info("SUCCESS: Opened the Link on the driver")
    except AssertionError:
        logging.error("ERROR: The link must be a valid string")


def company_search(driver, company_name):
    # NEED TO ADD TIMEFRAME Afterwards
    """
    Searches company name on the website opened

    :param driver: driver of Selenium described through function start_driver (WebElement)
    :param company_name: Company name (str)
    :return:
    """
    try:
        # Logging
        logging.info("company name = {} \n ".format(company_name))

        # Making sure the company name is a str
        assert isinstance(company_name, str)

        # Searches the Company Name
        driver.find_element_by_xpath('//*[@id="ssid"]').click()
        driver.find_element_by_xpath('//*[@id="ssid"]/option[1]').click()
        logging.info("SUCCESS: Changed to All-Sub-Section")
        driver.find_element_by_xpath('//*[@id="search"]').click()
        driver.find_element_by_xpath('//*[@id="search"]').send_keys(company_name)  # Company name
        logging.info("SUCCESS: Typed the company name successfully")
        driver.find_element_by_xpath('//*[@id="2"]/div[5]/div[1]/a').click()
        logging.info("SUCCESS: Searched the companies documents")
        time.sleep(1)
    except AssertionError:
        logging.error("ERROR: The company name must be a string")


def download_documents(driver):

    # Count of rows of documents clicked
    count = 1
    # Current window handle:
    win_handle_before = driver.current_window_handle
    try:
        while count < 25:

            # Finds the table rows and clicks
            driver.find_element_by_xpath('//*[@id="sample_1"]/tbody/tr[%d]/td[2]/a' % count).click()
            time.sleep(1)
            logging.info("SUCCESS: Clicked the" + count + "row Link")

            # get first child window
            change_window = driver.window_handles
            for w in change_window:
                # switch focus to child window
                if w != win_handle_before:
                    driver.switch_to.window(w)
            # find pdf url
            pdf_url = driver.find_element_by_tag_name('iframe').get_attribute("src")
            # load page with pdf
            driver.get(pdf_url)
            # download file
            download = driver.find_element_by_xpath('//*[@id="download"]')
            download.click()
            logging.info("SUCCESS: Downloaded the document")
            driver.close()
            logging.info("SUCCESS: Closed the " + count + "row Link")
            time.sleep(1)
            driver.switch_to.window(win_handle_before)
            count += 1
    except:
        pass
