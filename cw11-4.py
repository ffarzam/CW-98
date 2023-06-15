import logging


logger = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("application.log")

c_format = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s')
f_format = logging.Formatter('%(asctime)s || %(name)s || %(levelname)s || %(message)s')

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.setLevel(logging.DEBUG)

logger.warning('This is a warning message')
logger.error('This is an error message')