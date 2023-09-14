import inspect
import logging


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject_swaglabs\\Log\\swaglabs.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(lineno)d : %(message)s ")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
