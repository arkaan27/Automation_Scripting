"""
This is Selenium Library used to automate Downloads from link

Author: Arkaan Quanunga,

Date: 07/01/2022

"""
# Imports
import logging
import selenium
import os

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
    except AssertionError:
        logging.error("ERROR: The BASE PATH/ COMPANY NAME MUST BE A STR")

    try:


    # Checking the file already exists
    try:
        os.mkdir(download_path)
        logging.info("SUCCESS: Created the directory")
    except FileExistsError:
        logging.error("ERROR: This directory already exists")

    return download_path

# def start_driver(download_path,chrome_driver_path):
#     """
#     Starts the driver
#
#     :param download_path: download directory path (str)
#     :param chrome_driver_path: chrome driver path (str)
#     :return: driver
#     """
#
#
#
#
#
#
# def open_link(driver, link):
#
#
#
# def company_search(company_name, time_frame):
#
#
