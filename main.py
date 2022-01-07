import Selenium_Library as se
import logging


logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s'
)

if __name__ == '__main__':

    # Description of Base path
    base_path = 'D://'

    # Creating Directory
    download = se.create_directory(base_path, 1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
