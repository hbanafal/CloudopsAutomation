import inspect
import logging
import time
import os

def customLogger(logLevel=logging.DEBUG):

    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    # Creating logs directory
    fileName = "automation.log"
    logsDirectory = "../../../logs/"
    relativeFileName = logsDirectory + fileName
    currentDirectory = os.path.dirname(__file__)
    destinationFile = os.path.join(currentDirectory, relativeFileName)
    destinationDirectory = os.path.join(currentDirectory, logsDirectory)

    if not os.path.exists(destinationDirectory):
            os.makedirs(destinationDirectory)

    fileHandler = logging.FileHandler(destinationFile, mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
